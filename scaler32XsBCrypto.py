# ---------------------------------------------------------
# CTF CRYPTOGRAPHY
# ---------------------------------------------------------

import base64
import hashlib
import binascii


def crypto_base64_encode(text):
    """Encode text using Base64."""

    try:
        encoded = base64.b64encode(
            text.encode("utf-8")
        ).decode("utf-8")

        print_section("BASE64 ENCODE")

        print(f"  Input  : {text}")
        print(f"  Output : {encoded}")

    except Exception as error:
        print(f"  [!] Base64 encoding error: {error}")


def crypto_base64_decode(text):
    """Decode Base64 text."""

    try:
        decoded = base64.b64decode(
            text,
            validate=True
        ).decode("utf-8")

        print_section("BASE64 DECODE")

        print(f"  Input  : {text}")
        print(f"  Output : {decoded}")

    except (binascii.Error, UnicodeDecodeError):
        print("  [!] Invalid Base64 input.")


def crypto_md5(text):
    """Generate MD5 hash."""

    result = hashlib.md5(
        text.encode("utf-8")
    ).hexdigest()

    print_section("MD5")

    print(f"  Input : {text}")
    print(f"  Hash  : {result}")


def crypto_sha256(text):
    """Generate SHA-256 hash."""

    result = hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()

    print_section("SHA-256")

    print(f"  Input : {text}")
    print(f"  Hash  : {result}")


def crypto_sha512(text):
    """Generate SHA-512 hash."""

    result = hashlib.sha512(
        text.encode("utf-8")
    ).hexdigest()

    print_section("SHA-512")

    print(f"  Input : {text}")
    print(f"  Hash  : {result}")


def identify_hash(value):
    """
    Identify possible hash formats based on
    hexadecimal length.
    """

    print_section("HASH FORMAT IDENTIFICATION")

    value = value.strip()

    possibilities = []

    if len(value) == 32:
        possibilities.append("MD5")

    elif len(value) == 40:
        possibilities.append("SHA-1")

    elif len(value) == 64:
        possibilities.append("SHA-256")

    elif len(value) == 96:
        possibilities.append("SHA-384")

    elif len(value) == 128:
        possibilities.append("SHA-512")

    if all(c in "0123456789abcdefABCDEF" for c in value):

        if possibilities:

            print(f"  Input length : {len(value)}")
            print("  Possible format(s):")

            for item in possibilities:
                print(f"    [+] {item}")

            print(
                "\n  [!] This is format-based identification only."
            )

        else:

            print(
                "  [!] Hexadecimal value, "
                "but no common hash length matched."
            )

    else:

        print(
            "  [!] Input is not a standard hexadecimal hash."
        )


def crypto_all(text):
    """Generate common hashes for one input."""

    print_section("CTF CRYPTO ANALYSIS")

    print(f"  Input: {text}\n")

    md5_hash = hashlib.md5(
        text.encode()
    ).hexdigest()

    sha256_hash = hashlib.sha256(
        text.encode()
    ).hexdigest()

    sha512_hash = hashlib.sha512(
        text.encode()
    ).hexdigest()

    base64_value = base64.b64encode(
        text.encode()
    ).decode()

    print(f"  Base64 : {base64_value}")
    print(f"  MD5    : {md5_hash}")
    print(f"  SHA256 : {sha256_hash}")
    print(f"  SHA512 : {sha512_hash}")