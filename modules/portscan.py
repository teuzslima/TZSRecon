import socket
from datetime import datetime
from core.logger import log_event
from core.utils import normalize_host
from core.ui import print_live_header, progress_bar, box
try:
    from colorama import Fore
except Exception:
    class Fore:
        GREEN = RED = CYAN = YELLOW = WHITE = ""

COMMON_PORTS = {
    21: "ftp",
    22: "ssh",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    143: "imap",
    443: "https",
    3306: "mysql",
    5432: "postgresql",
    8080: "http-proxy",
}


def scan_port(target, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            service = COMMON_PORTS.get(port, "unknown")
            message = f"{port}/tcp".ljust(12) + Fore.GREEN + "OPEN".ljust(12) + Fore.WHITE + service
            print(message)
            log_event(f"[OPEN] Port {port} - {service}")
            return True

    except Exception as error:
        log_event(f"Error scanning port {port}: {error}")

    return False


def basic_scan(target):
    host = normalize_host(target)

    print_live_header("PORT SCAN")
    print(Fore.CYAN + f"TARGET: {host}")
    print(Fore.CYAN + f"TIME  : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

    progress_bar("STARTING PORT SCAN")

    print(Fore.GREEN + "PORT".ljust(12) + "STATE".ljust(12) + "SERVICE")
    print(Fore.GREEN + "-" * 42)

    open_ports = 0

    log_event(f"Basic scan started for {host}")

    for port in COMMON_PORTS:
        if scan_port(host, port):
            open_ports += 1

    summary = f"""SCAN COMPLETED
TARGET            : {host}
OPEN PORTS        : {open_ports}
CLOSED/FILTERED   : {len(COMMON_PORTS) - open_ports}
REPORT            : reports/scans/tzsrecon.log"""

    box("SCAN SUMMARY", summary, Fore.GREEN)
    log_event(f"Basic scan completed for {host}")
