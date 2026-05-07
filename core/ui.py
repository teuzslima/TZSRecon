from datetime import datetime
import os
import getpass
import platform
import shutil
import random
import time

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except Exception:
    class Empty:
        BLACK = RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = RESET_ALL = BRIGHT = DIM = ""
    Fore = Style = Empty()


LOGO = r"""
████████╗███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
╚══██╔══╝╚══███╔╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
   ██║     ███╔╝ ███████╗██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
   ██║    ███╔╝  ╚════██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
   ██║   ███████╗███████║██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
"""

MAP = r"""
        . . . . . . . . . . . . . . . . . . .
     . . . . . . . . . . . . . . . . . . . . . .
   . . . . . . . . . . . . . . . . . . . . . . .
       . . .  AMERICAS  . . .     EUROPE/ASIA
         . . .   ◎   . . .       . . . . . .
           . . . . . . . .       . . . . .
"""

def line(width=78):
    return "═" * width

def thin(width=78):
    return "─" * width

def box(title, content, color=Fore.GREEN, width=78):
    print(color + f"╔{line(width)}╗")
    print(color + f"║ > {title}".ljust(width + 1) + "║")
    print(color + f"╠{thin(width)}╣")
    for row in content.splitlines():
        print(color + "║ " + Fore.WHITE + row[:width-2].ljust(width-2) + color + " ║")
    print(color + f"╚{line(width)}╝")

def glitch_intro():
    chars = "01X#$@%&"
    phrase = "INITIALIZING TZSRECON FRAMEWORK"
    for _ in range(2):
        fake = "".join(random.choice(chars) if c != " " else " " for c in phrase)
        print(Fore.GREEN + fake)
        time.sleep(0.04)

def show_dashboard(target=None):
    os.system("clear" if os.name != "nt" else "cls")
    width = shutil.get_terminal_size((100, 30)).columns

    glitch_intro()

    print(Fore.GREEN + LOGO)
    print(Fore.CYAN + " " * 12 + "AUTOMATED SECURITY RECON FRAMEWORK")
    print(Fore.BLUE + " " * 10 + "[ AUTHOR: @TEUZSS ]   [ VERSION: 2.0.0 ]")
    print(Fore.YELLOW + " " * 18 + "⚠ AUTHORIZED TESTING ONLY ⚠\n")

    system_content = f"""RECON ENGINE      : ONLINE
MODULES LOADED    : 4/4
DATABASE          : LOCAL
LOGGING CORE      : ENABLED
UPDATE STATUS     : READY
SYSTEM            : {platform.system()}
USER              : {getpass.getuser()}
DATE              : {datetime.now().strftime('%d/%m/%Y')}
TIME              : {datetime.now().strftime('%H:%M:%S')}"""

    box("SYSTEM STATUS", system_content, Fore.GREEN)

    menu = """[1] ⚡ SCAN        Port Scanner
[2] 🔎 ENUM        Banner Grabbing
[3] 🌐 OSINT       Headers / WHOIS
[4] 📁 REPORTS     logs saved in reports/scans/
[0] 🚪 EXIT        Ctrl+C"""

    box("MAIN MENU", menu, Fore.CYAN)

def print_target_panel(target):
    content = f"""TARGET            : {target}
STATUS            : READY
MODE              : EDUCATIONAL
PERMISSION        : REQUIRED"""
    box("TARGET INFO", content, Fore.MAGENTA)

def print_help_panel():
    content = """python3 main.py -t 127.0.0.1 --scan
python3 main.py -t 127.0.0.1 --banner 80
python3 main.py -t example.com --headers
python3 main.py -t example.com --whois"""
    box("QUICKSTART", content, Fore.YELLOW)

def print_live_header(title):
    print(Fore.GREEN + f"\n╔{line(78)}╗")
    print(Fore.GREEN + f"║ > LIVE OUTPUT :: {title}".ljust(79) + "║")
    print(Fore.GREEN + f"╚{line(78)}╝")

def progress_bar(label="RUNNING", total=30):
    print(Fore.CYAN + f"[+] {label}")
    bar = ""
    for _ in range(total):
        bar += "█"
        print(Fore.GREEN + f"\r{bar:<30}  {int(len(bar)/total*100)}%", end="")
        time.sleep(0.01)
    print("\n")

def print_map():
    print(Fore.GREEN + MAP)
