"""Verify that a deployed web page returns the expected status and text."""

import argparse
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="HTTP or HTTPS URL to check")
    parser.add_argument("--status", type=int, default=200)
    parser.add_argument("--contains", help="Text expected on the page")
    args = parser.parse_args()

    if urlsplit(args.url).scheme not in ("http", "https"):
        parser.error("Use an http:// or https:// URL.")

    try:
        try:
            response = urlopen(args.url, timeout=10)
        except HTTPError as error:
            response = error
        with response:
            if response.status != args.status:
                print(f"Expected HTTP {args.status}, got {response.status}.", file=sys.stderr)
                return 1
            if args.contains is not None:
                charset = response.headers.get_content_charset() or "utf-8"
                body = response.read(1_048_576).decode(charset, errors="replace")
                if args.contains not in body:
                    print("Expected text missing from the first 1 MiB.", file=sys.stderr)
                    return 1
    except (URLError, OSError, LookupError, ValueError) as error:
        print(f"Check failed: {error}", file=sys.stderr)
        return 1

    print(f"OK (HTTP {args.status})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
