    # -----------------------------------------------------
    # Crypto / CTF
    # -----------------------------------------------------

    crypto_parser = subparsers.add_parser(
        "crypto",
        help="CTF cryptography and encoding utilities"
    )

    crypto_subparsers = crypto_parser.add_subparsers(
        dest="crypto_command"
    )

    # Base64 encode
    b64_encode_parser = crypto_subparsers.add_parser(
        "base64-encode",
        help="Encode text using Base64"
    )

    b64_encode_parser.add_argument(
        "text",
        help="Text to encode"
    )

    # Base64 decode
    b64_decode_parser = crypto_subparsers.add_parser(
        "base64-decode",
        help="Decode Base64"
    )

    b64_decode_parser.add_argument(
        "text",
        help="Base64 value"
    )

    # MD5
    md5_parser = crypto_subparsers.add_parser(
        "md5",
        help="Generate MD5 hash"
    )

    md5_parser.add_argument(
        "text",
        help="Text to hash"
    )

    # SHA256
    sha256_parser = crypto_subparsers.add_parser(
        "sha256",
        help="Generate SHA-256 hash"
    )

    sha256_parser.add_argument(
        "text",
        help="Text to hash"
    )

    # SHA512
    sha512_parser = crypto_subparsers.add_parser(
        "sha512",
        help="Generate SHA-512 hash"
    )

    sha512_parser.add_argument(
        "text",
        help="Text to hash"
    )

    # Hash identification
    identify_parser = crypto_subparsers.add_parser(
        "identify",
        help="Identify possible hash format"
    )

    identify_parser.add_argument(
        "value",
        help="Hash value"
    )

    # All crypto operations
    all_crypto_parser = crypto_subparsers.add_parser(
        "all",
        help="Generate Base64, MD5, SHA-256 and SHA-512"
    )

    all_crypto_parser.add_argument(
        "text",
        help="Text to analyze"
    )