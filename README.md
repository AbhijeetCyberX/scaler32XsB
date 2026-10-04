# scaler32XsB
A modular Python cybersecurity reconnaissance, OSINT, network scanning, and CTF utility toolkit for authorized security testing and learning.
scaler32XsB is a modular Python cybersecurity toolkit
designed for authorized security testing, reconnaissance,
OSINT, network analysis, and CTF learning.


cd scaler32XsB
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

scaler32XsB

Cybersecurity Reconnaissance & CTF Toolkit

scaler32XsB is a modular Python toolkit for authorized cybersecurity labs,
CTFs, reconnaissance, OSINT, network analysis, web reconnaissance,
cryptography utilities, and SSH administration.

Authorization: Use scanning, enumeration, SSH, and OSINT features only
against systems and networks you own or have explicit permission to test.

Architecture

scaler32XsB
│
├── scaler32XsB.py
├── modules/
│   ├── recon.py
│   ├── dns.py
│   ├── ports.py
│   ├── network.py
│   ├── subdomain.py
│   ├── osint.py
│   ├── location.py
│   ├── web_recon.py
│   ├── crypto.py
│   └── ssh_tool.py
├── wordlists/
├── reports/
└── tests/

Installation

git clone YOUR_REPOSITORY_URL
cd scaler32XsB
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Help

python3 scaler32XsB.py --help

Recon

python3 scaler32XsB.py url example.com
python3 scaler32XsB.py dns example.com
python3 scaler32XsB.py reverse-dns 8.8.8.8
python3 scaler32XsB.py dns-records example.com
python3 scaler32XsB.py web example.com
python3 scaler32XsB.py full example.com

Network

Only use these against authorized targets:

python3 scaler32XsB.py ports 192.168.1.10 --start 1 --end 1024
python3 scaler32XsB.py network 192.168.1.0/24

Subdomains

python3 scaler32XsB.py subdomains example.com -w wordlists/subdomains.txt

OSINT

python3 scaler32XsB.py location 8.8.8.8
python3 scaler32XsB.py whois example.com
python3 scaler32XsB.py shodan 8.8.8.8 --api-key YOUR_API_KEY

IP geolocation is approximate and should not be treated as an exact physical address.

CTF Crypto

python3 scaler32XsB.py crypto base64-encode "flag{hello}"
python3 scaler32XsB.py crypto base64-decode "ZmxhZ3toZWxsb30="
python3 scaler32XsB.py crypto base32-encode "hello"
python3 scaler32XsB.py crypto hex-encode "hello"
python3 scaler32XsB.py crypto hex-decode "68656c6c6f"
python3 scaler32XsB.py crypto ascii-to-binary "hello"
python3 scaler32XsB.py crypto binary-to-ascii "01101000 01100101 01101100 01101100 01101111"
python3 scaler32XsB.py crypto rot13 "uryyb"
python3 scaler32XsB.py crypto caesar "hello" --shift 3
python3 scaler32XsB.py crypto md5 "hello"
python3 scaler32XsB.py crypto sha256 "hello"
python3 scaler32XsB.py crypto sha512 "hello"
python3 scaler32XsB.py crypto identify "5d41402abc4b2a76b9719d911017c592"
python3 scaler32XsB.py crypto all "hello"

SSH

For authorized systems:

python3 scaler32XsB.py ssh 192.168.1.100 -u kali

The password is requested interactively so it is not exposed in shell history.

Testing

pytest

Future Features

JSON/HTML reports

TLS certificate inspection

robots.txt analysis

URL analysis

Certificate Transparency lookup

ASN information

service/banner detection

richer CTF encodings

plugin architecture

improved SSH terminal handling

configurable API keys through environment variables

License

MIT

python3 scaler32XsB.py --help

python3 scaler32XsB.py dns example.com
python3 scaler32XsB.py web example.com
python3 scaler32XsB.py crypto all "hello"
python3 scaler32XsB.py ports 192.168.1.10 --start 1 --end 1024
