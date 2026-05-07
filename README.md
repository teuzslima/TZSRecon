# TZSRecon - Automated Security Recon Framework

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

TZSRecon is an educational cybersecurity toolkit focused on reconnaissance, enumeration and authorized testing.

## Visual CLI

```text
> SYSTEM STATUS
RECON ENGINE      : ONLINE
MODULES LOADED    : 4/4
LOGGING CORE      : ENABLED

> MAIN MENU
[1] SCAN
[2] ENUM
[3] OSINT
[4] REPORTS
```

## Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 main.py -t 127.0.0.1 --scan
python3 main.py -t 127.0.0.1 --banner 80
python3 main.py -t example.com --headers
python3 main.py -t example.com --whois
```

## Legal Disclaimer

Use only in environments you own or have explicit authorization to test.
