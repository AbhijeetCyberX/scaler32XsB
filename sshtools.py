# modules/ssh_tool.py

import paramiko
import getpass
import socket


def ssh_connect(ip, username, password, port=22):
    """
    Connect to an SSH server using username/password.

    Intended for systems you own or are authorized to access.
    """

    print("\n" + "=" * 60)
    print("[+] SSH CONNECTION")
    print("=" * 60)

    print(f"  Host     : {ip}")
    print(f"  Port     : {port}")
    print(f"  Username : {username}")
    print("\n[+] Connecting...")

    client = paramiko.SSHClient()

    # Automatically accept the server's host key.
    # For production systems, verify host keys instead.
    client.set_missing_host_key_policy(
        paramiko.AutoAddPolicy()
    )

    try:

        client.connect(
            hostname=ip,
            port=port,
            username=username,
            password=password,
            timeout=10,
            allow_agent=False,
            look_for_keys=False
        )

        print("[+] SSH connection successful!")
        print("[+] Opening SSH terminal...\n")

        # Open an interactive shell
        channel = client.invoke_shell()

        # Transfer terminal input/output
        interactive_shell(channel)

    except paramiko.AuthenticationException:
        print("[!] Authentication failed.")
        print("[!] Check the username and password.")

    except paramiko.SSHException as error:
        print(f"[!] SSH error: {error}")

    except socket.timeout:
        print("[!] Connection timed out.")

    except socket.error as error:
        print(f"[!] Network error: {error}")

    finally:
        client.close()
        print("\n[+] SSH connection closed.")


def interactive_shell(channel):
    """
    Basic interactive terminal for the SSH session.
    """

    import select
    import sys
    import termios
    import tty

    old_settings = termios.tcgetattr(sys.stdin)

    try:

        tty.setraw(sys.stdin.fileno())

        while True:

            readable, _, _ = select.select(
                [channel, sys.stdin],
                [],
                []
            )

            if channel in readable:

                data = channel.recv(4096)

                if not data:
                    break

                sys.stdout.write(
                    data.decode(
                        "utf-8",
                        errors="ignore"
                    )
                )

                sys.stdout.flush()

            if sys.stdin in readable:

                command = sys.stdin.read(1)

                if not command:
                    break

                channel.send(command)

    except KeyboardInterrupt:
        print("\n[+] Closing SSH session...")

    finally:
        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            old_settings
        )
    from modules.ssh_tool import ssh_connect