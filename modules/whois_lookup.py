from core.utils import normalize_host
from core.logger import log_event
from core.ui import print_live_header, box
try:
    from colorama import Fore
except Exception:
    class Fore:
        GREEN = RED = CYAN = YELLOW = WHITE = ""

try:
    import whois
except ImportError:
    whois = None


def whois_lookup(target):
    host = normalize_host(target)
    print_live_header("WHOIS LOOKUP")

    if whois is None:
        print(Fore.RED + "[!] python-whois is not installed. Run: pip install python-whois")
        return

    try:
        data = whois.whois(host)
        box(f"WHOIS RESULT FOR {host}", str(data), Fore.GREEN)
        log_event(f"WHOIS lookup completed for {host}")

    except Exception as error:
        print(Fore.RED + f"[!] WHOIS lookup failed: {error}")
        log_event(f"WHOIS lookup failed for {host}: {error}")
