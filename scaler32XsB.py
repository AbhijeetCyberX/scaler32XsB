#!/usr/bin/env python3

import argparse
import socket
import sys
import ipaddress
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed


BANNER = r"""
   ███████╗ ██████╗ █████╗ ██╗     ███████╗██████╗
   ██╔════╝██╔════╝██╔══██╗██║     ██╔════╝╚════██╗
   ███████╗██║     ███████║██║     █████╗   ██████╔╝
   ╚════██║██║     ██╔══██║██║     ██╔══╝  ██╔═══╝
   ███████║╚██████╗██║  ██║███████╗███████╗██║
   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝

                 scaler32XsB
       Cybersecurity Reconnaissance Toolkit
"""


# ---------------------------------------------------------
# Utility functions
# ---------------------------------------------------------

def normalize_target(target):
    """Extract hostname from URL/domain."""
    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    parsed = urlparse(target)

    if not parsed.hostname:
        raise ValueError("Invalid URL or domain")

    return parsed.hostname


def print_section(title):
    print("\n" + "=" * 60)
    print(f"[+] {title}")
    print("=" * 60)


# ---------------------------------------------------------
# DNS / Domain Information
# ---------------------------------------------------------

def dns_lookup(domain):
    print_section("DNS INFORMATION")

    try:
        addresses = socket.getaddrinfo(domain, None)

        ips = sorted(
            set(
                result[4][0]
                for result in addresses
                if result[4]
            )
        )

        if ips:
            for ip in ips:
                print(f"  IP Address : {ip}")
        else:
            print("  No IP address found.")

    except socket.gaierror:
        print("  [!] DNS lookup failed.")


def reverse_dns(ip):
    print_section("REVERSE DNS")

    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"  IP       : {ip}")
        print(f"  Hostname : {hostname}")

    except socket.herror:
        print("  No reverse DNS record found.")


# ---------------------------------------------------------
# HTTP Information
# ---------------------------------------------------------

def http_information(domain):
    print_section("HTTP / HTTPS INFORMATION")

    for scheme in ["https", "http"]:
        url = f"{scheme}://{domain}"

        try:
            response = requests.get(
                url,
                timeout=5,
                allow_redirects=True
            )

            print(f"\n  URL           : {url}")
            print(f"  Status        : {response.status_code}")
            print(f"  Final URL     : {response.url}")
            print(f"  Server        : {response.headers.get('Server', 'Unknown')}")
            print(f"  Content-Type  : {response.headers.get('Content-Type', 'Unknown')}")
            print(f"  Technologies  : {response.headers.get('X-Powered-By', 'Unknown')}")

            break

        except requests.RequestException:
            continue


# ---------------------------------------------------------
# IP Geolocation
# ---------------------------------------------------------

def ip_location(ip):
    print_section("IP GEOLOCATION")

    try:
        response = requests.get(
            f"https://ipinfo.io/{ip}/json",
            timeout=5
        )

        data = response.json()

        print(f"  IP       : {data.get('ip', 'Unknown')}")
        print(f"  City     : {data.get('city', 'Unknown')}")
        print(f"  Region   : {data.get('region', 'Unknown')}")
        print(f"  Country  : {data.get('country', 'Unknown')}")
        print(f"  Location : {data.get('loc', 'Unknown')}")
        print(f"  ISP/Org  : {data.get('org', 'Unknown')}")
        print(f"  Timezone : {data.get('timezone', 'Unknown')}")

    except requests.RequestException:
        print("  [!] Could not retrieve geolocation information.")


# ---------------------------------------------------------
# Subdomain Enumeration
# ---------------------------------------------------------

def check_subdomain(subdomain, domain):
    hostname = f"{subdomain}.{domain}"

    try:
        ip = socket.gethostbyname(hostname)
        return hostname, ip

    except socket.gaierror:
        return None


def subdomain_scan(domain, wordlist):
    print_section("SUBDOMAIN ENUMERATION")

    try:
        with open(wordlist, "r") as file:
            subdomains = [
                line.strip()
                for line in file
                if line.strip()
            ]

    except FileNotFoundError:
        print(f"  [!] Wordlist not found: {wordlist}")
        return

    found = []

    with ThreadPoolExecutor(max_workers=20) as executor:

        tasks = [
            executor.submit(
                check_subdomain,
                subdomain,
                domain
            )
            for subdomain in subdomains
        ]

        for task in as_completed(tasks):
            result = task.result()

            if result:
                hostname, ip = result
                found.append((hostname, ip))
                print(f"  [FOUND] {hostname:<35} {ip}")

    print(f"\n  Total subdomains found: {len(found)}")


# ---------------------------------------------------------
# TCP Port Scanner
# ---------------------------------------------------------

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((ip, port))

        if result == 0:
            return port

    except socket.error:
        pass

    finally:
        sock.close()

    return None


def port_scan(target, start_port, end_port):
    print_section("TCP PORT SCAN")

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("  [!] Could not resolve target.")
        return

    print(f"  Target IP: {ip}")
    print(f"  Ports: {start_port}-{end_port}\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=50) as executor:

        tasks = {
            executor.submit(
                scan_port,
                ip,
                port
            ): port
            for port in range(start_port, end_port + 1)
        }

        for task in as_completed(tasks):
            port = task.result()

            if port:
                open_ports.append(port)

    for port in sorted(open_ports):
        service = socket.getservbyport(port, "tcp") \
            if port <= 65535 else "unknown"

        print(f"  [OPEN] {port:<6} {service}")

    print(f"\n  Open ports found: {len(open_ports)}")


# ---------------------------------------------------------
# Local Network Scanner
# ---------------------------------------------------------

def ping_host(ip):
    """
    Basic TCP-based host discovery.
    Checks common ports rather than sending ICMP.
    """

    common_ports = [22, 80, 443, 445, 3389]

    for port in common_ports:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.2)

        try:
            if sock.connect_ex((str(ip), port)) == 0:
                return str(ip)

        finally:
            sock.close()

    return None


def network_scan(network):
    print_section("NETWORK DISCOVERY")

    try:
        net = ipaddress.ip_network(
            network,
            strict=False
        )
    except ValueError:
        print("  [!] Invalid network.")
        return

    print(f"  Network: {net}\n")

    found = []

    with ThreadPoolExecutor(max_workers=50) as executor:

        tasks = [
            executor.submit(ping_host, ip)
            for ip in net.hosts()
        ]

        for task in as_completed(tasks):

            result = task.result()

            if result:
                found.append(result)
                print(f"  [ACTIVE] {result}")

    print(f"\n  Active hosts found: {len(found)}")


# ---------------------------------------------------------
# Shodan
# ---------------------------------------------------------

def shodan_lookup(ip, api_key):
    print_section("SHODAN LOOKUP")

    if not api_key:
        print("  [!] Shodan API key required.")
        print("  Use: --shodan IP --api-key YOUR_KEY")
        return

    url = f"https://api.shodan.io/shodan/host/{ip}"

    try:
        response = requests.get(
            url,
            params={"key": api_key},
            timeout=10
        )

        if response.status_code != 200:
            print(f"  [!] Shodan returned HTTP {response.status_code}")
            return

        data = response.json()

        print(f"  IP       : {data.get('ip_str', ip)}")
        print(f"  Country  : {data.get('country_name', 'Unknown')}")
        print(f"  City     : {data.get('city', 'Unknown')}")
        print(f"  ISP      : {data.get('isp', 'Unknown')}")
        print(f"  OS       : {data.get('os', 'Unknown')}")

        ports = data.get("ports", [])

        print(f"  Ports    : {ports}")

        print("\n  Services:")

        for item in data.get("data", []):
            port = item.get("port", "Unknown")
            product = item.get("product", "Unknown")
            version = item.get("version", "")

            print(
                f"    {port:<6} "
                f"{product} {version}"
            )

    except requests.RequestException as error:
        print(f"  [!] Shodan request failed: {error}")


# ---------------------------------------------------------
# Full Recon
# ---------------------------------------------------------

def full_scan(target):
    domain = normalize_target(target)

    print_section("TARGET")
    print(f"  Domain : {domain}")

    try:
        ip = socket.gethostbyname(domain)
        print(f"  IP     : {ip}")
    except socket.gaierror:
        print("  [!] Could not resolve domain.")
        return

    dns_lookup(domain)
    reverse_dns(ip)
    http_information(domain)
    ip_location(ip)


# ---------------------------------------------------------
# CLI
# ---------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        prog="scaler32XsB",
        description=(
            "scaler32XsB - Cybersecurity "
            "Reconnaissance and OSINT Toolkit"
        )
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # URL scan
    url_parser = subparsers.add_parser(
        "url",
        help="Scan URL/domain information"
    )

    url_parser.add_argument(
        "target",
        help="URL or domain"
    )

    # DNS
    dns_parser = subparsers.add_parser(
        "dns",
        help="Perform DNS lookup"
    )

    dns_parser.add_argument(
        "domain",
        help="Domain name"
    )

    # Location
    loc_parser = subparsers.add_parser(
        "location",
        help="Find approximate IP location"
    )

    loc_parser.add_argument(
        "ip",
        help="IP address"
    )

    # Subdomain
    sub_parser = subparsers.add_parser(
        "subdomains",
        help="Enumerate subdomains"
    )

    sub_parser.add_argument(
        "domain",
        help="Target domain"
    )

    sub_parser.add_argument(
        "-w",
        "--wordlist",
        default="subdomains.txt",
        help="Subdomain wordlist"
    )

    # Port scanner
    port_parser = subparsers.add_parser(
        "ports",
        help="TCP port scan"
    )

    port_parser.add_argument(
        "target",
        help="IP or domain"
    )

    port_parser.add_argument(
        "--start",
        type=int,
        default=1
    )

    port_parser.add_argument(
        "--end",
        type=int,
        default=1024
    )

    # Network scanner
    net_parser = subparsers.add_parser(
        "network",
        help="Discover hosts on an authorized network"
    )

    net_parser.add_argument(
        "network",
        help="Example: 192.168.1.0/24"
    )

    # Shodan
    shodan_parser = subparsers.add_parser(
        "shodan",
        help="Query Shodan for an IP"
    )

    shodan_parser.add_argument(
        "ip",
        help="IP address"
    )

    shodan_parser.add_argument(
        "--api-key",
        required=True,
        help="Your Shodan API key"
    )

    # Full scan
    full_parser = subparsers.add_parser(
        "full",
        help="Perform full reconnaissance"
    )

    full_parser.add_argument(
        "target",
        help="URL or domain"
    )

    args = parser.parse_args()

    print(BANNER)

    if args.command == "url":
        full_scan(args.target)

    elif args.command == "dns":
        dns_lookup(args.domain)

    elif args.command == "location":
        ip_location(args.ip)

    elif args.command == "subdomains":
        subdomain_scan(
            args.domain,
            args.wordlist
        )

    elif args.command == "ports":
        port_scan(
            args.target,
            args.start,
            args.end
        )

    elif args.command == "network":
        network_scan(args.network)

    elif args.command == "shodan":
        shodan_lookup(
            args.ip,
            args.api_key
        )

    elif args.command == "full":
        full_scan(args.target)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()