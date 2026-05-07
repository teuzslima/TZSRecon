import requests
from core.utils import normalize_host
from core.logger import log_event
from core.ui import print_live_header, box
try:
    from colorama import Fore
except Exception:
    class Fore:
        GREEN = RED = CYAN = YELLOW = WHITE = ""


def http_headers(target):
    host = normalize_host(target)
    print_live_header("HTTP HEADERS")

    for scheme in ["https", "http"]:
        url = f"{scheme}://{host}"
        try:
            response = requests.get(url, timeout=5)
            content = ""
            for header, value in response.headers.items():
                content += f"{header}: {value}\n"

            box(f"HEADERS FOR {url}", content.strip(), Fore.CYAN)
            log_event(f"HTTP headers collected for {url}")
            return

        except requests.RequestException:
            continue

    print(Fore.RED + "[!] Could not collect HTTP headers")
    log_event(f"HTTP header collection failed for {host}")
