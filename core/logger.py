from datetime import datetime
from pathlib import Path

LOG_DIR = Path("reports/scans")
LOG_FILE = LOG_DIR / "tzsrecon.log"


def log_event(message):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")
