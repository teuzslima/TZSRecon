<div align="center">

# 🛰️ TZSRecon — Automated Security Recon Framework

**Toolkit de reconhecimento e enumeração para testes de segurança autorizados**
*Reconnaissance & enumeration toolkit for authorized security testing*

![Python](https://img.shields.io/badge/python-3.8+-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Purpose](https://img.shields.io/badge/purpose-educational-blueviolet)

[**Português**](#-português) · [**English**](#-english)

```text
> SYSTEM STATUS
RECON ENGINE      : ONLINE
MODULES LOADED    : 4/4
LOGGING CORE      : ENABLED

> MAIN MENU
[1] SCAN      [2] ENUM      [3] OSINT      [4] REPORTS
```

</div>

> ⚠️ **Uso autorizado apenas.** Utilize somente em ambientes que você possui ou tem
> permissão explícita para testar. / **Authorized use only** — see the disclaimer below.

---

## 🇧🇷 Português

### Sobre

**TZSRecon** é um framework de linha de comando, escrito em Python, para a fase de
**reconhecimento** em testes de segurança autorizados e estudo de cibersegurança. Reúne
módulos de varredura, captura de banner, OSINT e WHOIS numa CLI com dashboard visual e
registro de eventos (logging).

### Módulos

| Módulo | O que faz |
| --- | --- |
| 🔍 **Port Scan** | Varredura das portas comuns do alvo |
| 🏷️ **Banner Grab** | Captura o banner de uma porta específica |
| 🧭 **OSINT / Headers** | Coleta os cabeçalhos HTTP de segurança |
| 🌐 **WHOIS** | Consulta WHOIS básica do domínio |

### Instalação

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Uso

```bash
python3 main.py -t 127.0.0.1 --scan        # varredura de portas comuns
python3 main.py -t 127.0.0.1 --banner 80   # banner da porta 80
python3 main.py -t example.com --headers   # cabeçalhos HTTP de segurança
python3 main.py -t example.com --whois     # consulta WHOIS
```

**Stack:** Python 3.8+ · `requests` · `python-whois` · `colorama`.

---

## 🇺🇸 English

### About

**TZSRecon** is a Python command-line framework for the **reconnaissance** phase of
authorized security testing and cybersecurity study. It bundles port scanning, banner
grabbing, OSINT and WHOIS into a single CLI with a visual dashboard and event logging.

### Modules

| Module | What it does |
| --- | --- |
| 🔍 **Port Scan** | Scans the target's common ports |
| 🏷️ **Banner Grab** | Grabs the banner from a specific port |
| 🧭 **OSINT / Headers** | Collects HTTP security headers |
| 🌐 **WHOIS** | Basic domain WHOIS lookup |

### Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

```bash
python3 main.py -t 127.0.0.1 --scan        # common-ports scan
python3 main.py -t 127.0.0.1 --banner 80   # grab banner from port 80
python3 main.py -t example.com --headers   # HTTP security headers
python3 main.py -t example.com --whois     # WHOIS lookup
```

**Stack:** Python 3.8+ · `requests` · `python-whois` · `colorama`.

---

## ⚖️ Legal / Aviso legal

This tool is provided for **educational purposes** and **authorized testing only**. Use it
exclusively on systems you own or have **explicit written permission** to assess.
Unauthorized scanning or testing may be illegal. The author assumes no liability for misuse.

*Ferramenta para fins **educacionais** e **testes autorizados**. Use apenas em sistemas que
você possui ou tem **autorização explícita** para avaliar. O uso não autorizado pode ser
ilegal; o autor não se responsabiliza por mau uso.*

---

<div align="center">

MIT License · Desenvolvido por **[@teuzslima](https://github.com/teuzslima)**

</div>
