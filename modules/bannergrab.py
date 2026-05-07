import socket
from core.logger import log_event
from core.utils import normalize_host
from core.ui import print_live_header, box
try:
    from colorama import Fore
except Exception:
    class Fore:
        GREEN = RED = CYAN = YELLOW = WHITE = ""


def banner_grab(target, port):
    host = normalize_host(target)
    print_live_header("BANNER GRABBING")

    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((host, port))

        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()

            if banner:
                content = f"{host}:{port} -> {banner}"
            else:
                content = f"No banner returned from {host}:{port}"

            box("BANNER RESULT", content, Fore.CYAN)
            log_event(content)

        except Exception:
            print(Fore.YELLOW + "[!] Could not read banner")

        sock.close()

    except Exception as error:
        print(Fore.RED + f"[!] Connection failed: {error}")
        log_event(f"Banner grab failed for {host}:{port} - {error}")
