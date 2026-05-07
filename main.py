#!/usr/bin/env python3

import argparse
from datetime import datetime
from core.ui import show_dashboard, print_target_panel, print_help_panel
from core.logger import log_event
from modules.portscan import basic_scan
from modules.bannergrab import banner_grab
from modules.osint import http_headers
from modules.whois_lookup import whois_lookup


def main():
    parser = argparse.ArgumentParser(
        description="TZSRecon - Automated Security Recon Framework"
    )

    parser.add_argument("-t", "--target", help="Authorized target. Example: 127.0.0.1 or example.com")
    parser.add_argument("--scan", action="store_true", help="Run basic common port scan")
    parser.add_argument("--banner", type=int, help="Grab banner from a specific port")
    parser.add_argument("--headers", action="store_true", help="Get HTTP security headers")
    parser.add_argument("--whois", action="store_true", help="Run basic WHOIS lookup")

    args = parser.parse_args()

    show_dashboard(args.target)

    if not args.target:
        print_help_panel()
        return

    print_target_panel(args.target)
    log_event(f"Target selected: {args.target}")

    if args.scan:
        basic_scan(args.target)

    if args.banner:
        banner_grab(args.target, args.banner)

    if args.headers:
        http_headers(args.target)

    if args.whois:
        whois_lookup(args.target)

    if not args.scan and not args.banner and not args.headers and not args.whois:
        print_help_panel()


if __name__ == "__main__":
    main()
