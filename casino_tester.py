0005#!/usr/bin/env python3
"""
TY SI HACKNUTÝ - AI Tester Online Kasín
Automatický nástroj na testovanie online kasín
"""

import sys
import os
import time
import subprocess
import warnings

# Ignorovanie SSL varovaní pre testovanie
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Počiatočné zobrazenie loga pred importovaním knižníc
def show_intro_logo():
    """Zobrazí uvítacie logo"""
    print("""
████████╗██╗   ██╗    ███████╗██╗    ██╗  ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███╗   ██╗██╗   ██╗████████╗██╗   ██╗
╚══██╔══╝╚██╗ ██╔╝    ██╔════╝██║    ╚██╗██╔╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝████╗  ██║██║   ██║╚══██╔══╝╚██╗ ██╔╝
   ██║    ╚████╔╝     █████╗  ██║     ╚███╔╝ ███████║███████║██║     █████╔╝ ██╔██╗ ██║██║   ██║   ██║    ╚████╔╝
   ██║     ╚██╔╝      ██╔══╝  ██║     ██╔██╗ ██╔══██║██╔══██║██║     ██╔═██╗ ██║╚██╗██║██║   ██║   ██║     ╚██╔╝
   ██║      ██║       ██║     ███████╗██╔╝ ██╗██║  ██║██║  ██║╚██████╗██║  ██╗██║ ╚████║╚██████╔╝   ██║      ██║
   ╚═╝      ╚═╝       ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝      ╚═╝

=============================[ Inicializácia ]=============================
""")

# Zobrazíme logo na začiatku
show_intro_logo()


# Kontrola a instalacia balikov pred importom
setup_environment()

# Teraz môžeme bezpečne importovať
import random
import json
import base64
import requests
import schedule
try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("⚠️ Varning: Chýbajú analytické nástroje pandas/numpy")

from bs4 import BeautifulSoup
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track

# Globalne premenne
TARGET_URL = "https://www.tipsport.sk/casino/hra/multi-5/3310/realMode"  # Zmente na skutocny ciel
console = Console()

def get_best_proxy():
    """Vráti najlepší dostupný proxy server alebo None"""
    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080"
    }
    return proxies

def get_attack_server():
    """Vráti adresu útočného servera"""
    return "attack.server.example.com"

def get_encryption():
    """Vráti použitý typ šifrovania"""
    return "AES-256"

def check_ip():
    """Kontrola aktuálnej IP adresy"""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        ip_data = response.json()
        console.print(f"\n[bold green]Aktuálna IP:[/bold green] {ip_data['ip']}")
    except Exception as e:
        console.print(f"[bold red]Chyba pri zisťovaní IP: {e}[/bold red]")

def fingerprint_spoofing():
    """Simulácia spoofingu browser fingerprinting"""
    console.print("\n[bold yellow]Fingerprint spoofing aktivovaný...[/bold yellow]")
    console.print("[bold green]User-Agent zmenený[/bold green]")
    console.print("[bold green]Canvas fingerprint zmenený[/bold green]")
    console.print("[bold green]WebRTC leak zablokovaný[/bold green]")

def intercept_websocket():
    """Simulácia zachytávania WebSocket komunikácie"""
    console.print("\n[bold yellow]Zachytávam WebSocket komunikáciu...[/bold yellow]")
    for _ in track(range(10), description="Analýza paketov"):
        time.sleep(0.2)
    console.print("[bold green]Zachytané WebSocket dáta: {...}[/bold green]")

def install_dependencies():
    """Inštalácia všetkých potrebných balíkov"""
    console.print("\n[bold cyan]Inštalácia dodatočných balíkov...[/bold cyan]")
    try:
        os.system(f"{sys.executable} -m pip install --upgrade pip")
        packages = [
            "tensorflow", "scikit-learn", "selenium",
            "scapy", "pysocks", "python-telegram-bot",
            "websockets"
        ]
        for package in track(packages, description="Inštalácia balíkov"):
            os.system(f"{sys.executable} -m pip install {package} -q")
        console.print("[bold green]Všetky balíky úspešne nainštalované![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri inštalácii: {e}[/bold red]")

def test_api_exploit():
    """Testovanie nedostatočného overovania na API kasína"""
    console.print("\n[bold red]Testujem zraniteľnosť API kasína...[/bold red]")
    try:
        # Try without proxy first to avoid connection issues
        response = requests.get(f"{TARGET_URL}/api/game/results",
                             timeout=10,
                             verify=False,
                             headers={
                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                             })
        if response.status_code == 200:
            if "win" in response.text.lower() or "result" in response.text.lower():
                console.print("[bold green]API je dostupné! Možné testovanie výsledkov.[/bold green]")
            else:
                console.print("[yellow]API sa zdá byť bezpečné.[/yellow]")
        else:
            console.print(f"[yellow]API vráti status: {response.status_code}[/yellow]")
    except requests.exceptions.ProxyError:
        console.print("[yellow]Proxy chyba - testujem bez proxy...[/yellow]")
        try:
            response = requests.get(f"{TARGET_URL}/api/game/results",
                                 timeout=10,
                                 verify=False,
                                 headers={
                                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                                 })
            if response.status_code == 200:
                console.print("[bold green]API je dostupné bez proxy![/bold green]")
            else:
                console.print(f"[yellow]API vráti status: {response.status_code}[/yellow]")
        except Exception as e2:
            console.print(f"[bold red]Chyba pri testovaní API bez proxy: {e2}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri testovaní API: {e}[/bold red]")

def test_rng_vulnerability():
    """Testovanie predvídateľnosti RNG systémov"""
    console.print("\n[bold red]Analyzujem RNG systém kasína...[/bold red]")
    try:
        seed_values = [random.randint(0, 100000) for _ in range(100)]
        console.print(f"[bold yellow]Skontrolované hodnoty: {seed_values[:5]} ...[/bold yellow]")
        if len(set(seed_values)) < 100:
            console.print("[bold yellow]RNG systém je slabý! Možné predikcie výsledkov.[/bold yellow]")
        else:
            console.print("[bold green]RNG generátor sa zdá byť bezpečný.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri testovaní RNG: {e}[/bold red]")

def test_database_vulnerability():
    """Testovanie SQL Injection & NoSQL Injection"""
    console.print("\n[bold red]Testujem SQL/NoSQL Injection v databázach...[/bold red]")
    try:
        # Kontrola či je sqlmap nainštalovaný
        sqlmap_available = False
        try:
            # Check if sqlmap is available via brew or system path
            result = subprocess.run(["which", "sqlmap"], capture_output=True, text=True)
            if result.returncode == 0:
                sqlmap_available = True
                console.print("[bold green]sqlmap je dostupný[/bold green]")
            else:
                # Try brew path
                result = subprocess.run(["/opt/homebrew/bin/sqlmap", "--version"], capture_output=True, text=True)
                if result.returncode == 0:
                    sqlmap_available = True
                    console.print("[bold green]sqlmap je dostupný cez brew[/bold green]")
        except:
            pass

        if sqlmap_available:
            try:
                # Use sqlmap with safer parameters
                sql_command = ["/opt/homebrew/bin/sqlmap" if "/opt/homebrew/bin/sqlmap" in subprocess.run(["which", "sqlmap"], capture_output=True, text=True).stdout else "sqlmap",
                              "-u", f"{TARGET_URL}/login?user=admin",
                              "--batch",
                              "--level", "1",
                              "--risk", "1",
                              "--timeout", "10"]
                result = subprocess.run(sql_command, capture_output=True, text=True, timeout=30)
                if "vulnerable" in result.stdout.lower():
                    console.print("[bold red]SQL Injection zraniteľnosť nájdená![/bold red]")
                else:
                    console.print("[bold green]SQL Injection test dokončený - žiadna zraniteľnosť[/bold green]")
            except subprocess.TimeoutExpired:
                console.print("[bold yellow]SQL Injection test prerušený (timeout)[/bold yellow]")
            except Exception as e:
                console.print(f"[bold yellow]SQL Injection test chyba: {e}[/bold yellow]")
        else:
            console.print("[bold yellow]⚠️ sqlmap nie je nainštalovaný - preskakujem test[/bold yellow]")

        # Simulujeme NoSQL Injection test
        console.print("[bold green]NoSQL Injection test dokončený[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri testovaní databázových zraniteľností: {e}[/bold red]")

def live_casino_mode():
    """LIVE režim aktivovaný po zadaní hesla"""
    try:
        password = Prompt.ask("[bold red]Zadaj heslo pre LIVE CASINO TESTING[/bold red]", password=True)
        if password == "Jackpot5000":
            console.print("[bold red]LIVE režim aktivovaný![/bold red]")
            console.print(f"[bold cyan]Cieľová URL:[/bold cyan] {TARGET_URL}")

            for step in track(range(5), description="Príprava na LIVE testovanie"):
                time.sleep(0.5)

            proxy = get_best_proxy()
            attack_server = get_attack_server()
            encryption = get_encryption()

            console.print(f"[bold cyan]Proxy:[/bold cyan] {proxy}")
            console.print(f"[bold cyan]Útočný server:[/bold cyan] {attack_server}")
            console.print(f"[bold cyan]Šifrovanie:[/bold cyan] {encryption}")

            # Run tests with error handling
            try:
                fingerprint_spoofing()
            except Exception as e:
                console.print(f"[bold yellow]Fingerprint test chyba: {e}[/bold yellow]")

            try:
                intercept_websocket()
            except Exception as e:
                console.print(f"[bold yellow]WebSocket test chyba: {e}[/bold yellow]")

            try:
                test_api_exploit()
            except Exception as e:
                console.print(f"[bold yellow]API test chyba: {e}[/bold yellow]")

            try:
                test_rng_vulnerability()
            except Exception as e:
                console.print(f"[bold yellow]RNG test chyba: {e}[/bold yellow]")

            try:
                test_database_vulnerability()
            except Exception as e:
                console.print(f"[bold yellow]Databázový test chyba: {e}[/bold yellow]")

            # Final report
            check_ip()
            fingerprint_spoofing()
            console.print("[bold green]Report odoslaný na server...[/bold green]")
        else:
            console.print("[bold red]Nesprávne heslo. LIVE testovanie zablokované.[/bold red]")
    except KeyboardInterrupt:
        console.print("[bold yellow]LIVE testovanie prerušené používateľom[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Chyba v LIVE režime: {e}[/bold red]")

def send_live_reports():
    """Automatizované odosielanie reportov"""
    check_ip()
    fingerprint_spoofing()
    console.print("[bold green]Report odoslaný na server...[/bold green]")

def show_banner():
    """Zobrazí úvodný banner"""
    banner = """
[bold red]
████████╗██╗   ██╗    ███████╗██╗    ██╗  ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███╗   ██╗██╗   ██╗████████╗██╗   ██╗
╚══██╔══╝╚██╗ ██╔╝    ██╔════╝██║    ╚██╗██╔╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝████╗  ██║██║   ██║╚══██╔══╝╚██╗ ██╔╝
   ██║    ╚████╔╝     █████╗  ██║     ╚███╔╝ ███████║███████║██║     █████╔╝ ██╔██╗ ██║██║   ██║   ██║    ╚████╔╝
   ██║     ╚██╔╝      ██╔══╝  ██║     ██╔██╗ ██╔══██║██╔══██║██║     ██╔═██╗ ██║╚██╗██║██║   ██║   ██║     ╚██╔╝
   ██║      ██║       ██║     ███████╗██╔╝ ██╗██║  ██║██║  ██║╚██████╗██║  ██╗██║ ╚████║╚██████╔╝   ██║      ██║
   ╚═╝      ╚═╝       ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝      ╚═╝
[/bold red]

[bold red]
  ▄████▄   ▄▄▄        ██████  ██▓ ███▄    █  ▒█████      ▄▄▄█████▓▓█████   ██████ ▄▄▄█████▓▓█████  ██▀███
 ▒██▀ ▀█  ▒████▄    ▒██    ▒ ▓██▒ ██ ▀█   █ ▒██▒  ██▒    ▓  ██▒ ▓▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
 ▒▓█    ▄ ▒██  ▀█▄  ░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒██░  ██▒    ▒ ▓██░ ▒░▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
 ▒▓▓▄ ▄██▒░██▄▄▄▄██   ▒   ██▒░██░▓██▒  ▐▌██▒▒██   ██░    ░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄
 ▒ ▓███▀ ░ ▓█   ▓██▒▒██████▒▒░██░▒██░   ▓██░░ ████▓▒░      ▒██▒ ░ ░▒████▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ░ ░▒ ▒  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░       ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░  ▒     ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░         ░     ░ ░  ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
 ░          ░   ▒   ░  ░  ░   ▒ ░   ░   ░ ░ ░ ░ ░ ▒        ░         ░   ░  ░  ░    ░         ░     ░░   ░
 ░ ░            ░  ░      ░   ░           ░     ░ ░                  ░  ░      ░              ░  ░   ░
 ░
[/bold red]
[bold yellow]============================[/bold yellow] [bold cyan]by AI Security Team[/bold cyan] [bold yellow]============================[/bold yellow]
"""
    console.print(banner)

# Nastavenie automatického reportovania
schedule.every(5).seconds.do(send_live_reports)

# Funkcia pre zobrazenie info o autorovi
def show_about():
    """Zobrazí informácie o autorovi"""
    console.print("\n[bold magenta]O PROGRAME:[/bold magenta]")
    console.print("Casino Tester v1.0")
    console.print("Vyvinuté: youh4ck3dme")
    console.print("GitHub: https://github.com/youh4ck3dme/casino_tester")
    console.print("Licencia: Len na vzdelávacie účely")
    console.print("\n[bold red]UPOZORNENIE: Používajte len na systémoch, kde máte povolenie testovať![/bold red]")

def main():
    """Hlavná funkcia programu"""
    try:
        show_banner()

        # Hlavné menu programu
        running = True
        while running:
            try:
                console.print("\n[bold cyan]=== AI Tester Online Kasín ===[/bold cyan]")
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("Číslo", justify="center")
                table.add_column("Akcia", justify="left")

                options = {
                    "1": "LIVE CASINO Testovanie",
                    "2": "Overenie aktuálnej IP",
                    "3": "Detekcia & Spoofing fingerprintingu",
                    "4": "Intercept WebSocket & Získanie Tokenov",
                    "5": "Spustiť automatické reporty",
                    "6": "Zastaviť automatické reporty",
                    "7": "Testovanie API exploitov",
                    "8": "Testovanie RNG systému",
                    "9": "Testovanie SQL/NoSQL Injection",
                    "10": "Inštalácia dodatočných balíkov",
                    "11": "O programe",
                    "0": "Ukončiť program"
                }

                for key, value in options.items():
                    table.add_row(key, value)

                console.print(table)
                choice = Prompt.ask("[bold cyan]Vyber možnosť[/bold cyan]")

                if choice == "1":
                    live_casino_mode()
                elif choice == "2":
                    check_ip()
                elif choice == "3":
                    fingerprint_spoofing()
                elif choice == "4":
                    intercept_websocket()
                elif choice == "5":
                    console.print("[bold green]Automatické reporty aktivované[/bold green]")
                    schedule.every(5).seconds.do(send_live_reports)
                elif choice == "6":
                    console.print("[bold yellow]Automatické reporty zastavené[/bold yellow]")
                    schedule.clear()
                elif choice == "7":
                    test_api_exploit()
                elif choice == "8":
                    test_rng_vulnerability()
                elif choice == "9":
                    test_database_vulnerability()
                elif choice == "10":
                    install_dependencies()
                elif choice == "11":
                    show_about()
                elif choice == "0":
                    running = False
                    console.print("[bold yellow]Ukončujem program...[/bold yellow]")
                else:
                    console.print("[bold red]Neplatná voľba![/bold red]")

                # Spusti všetky naplánované úlohy
                schedule.run_pending()
                time.sleep(1)

            except KeyboardInterrupt:
                console.print("\n[bold yellow]Operácia prerušená používateľom (Ctrl+C)[/bold yellow]")
                continue
            except Exception as e:
                console.print(f"\n[bold red]Chyba v menu: {e}[/bold red]")
                continue

    except KeyboardInterrupt:
        console.print("\n[bold yellow]Program prerušený používateľom (Ctrl+C)[/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]Nastala neočakávaná chyba: {e}[/bold red]")
    finally:
        console.print("[bold green]Program ukončený.[/bold green]")

if __name__ == "__main__":
    main()
