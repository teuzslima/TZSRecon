#!/bin/bash

echo "[+] Creating virtual environment..."
python3 -m venv venv

echo "[+] Activating virtual environment..."
source venv/bin/activate

echo "[+] Installing dependencies..."
pip install -r requirements.txt

echo "[+] Installation completed."
echo "[*] Run: source venv/bin/activate"
echo "[*] Run: python3 main.py -t 127.0.0.1 --scan"
