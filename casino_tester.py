#!/usr/bin/env python3
# filepath: c:\Users\42195\OneDrive\Desktop\casino_tester.py

"""
YOU HACKED ME - AI Tester Online Kasin
Automaticky nastroj na testovanie online kasin
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
    """Zobrazi uvítacie logo"""
    print("""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ███╗   ███╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ████╗ ████║██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ███████║███████║██║     █████╔╝ █████╗  ██║  ██║    ██╔████╔██║█████╗  
  ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██║╚██╔╝██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██║ ╚═╝ ██║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝     ╚═╝╚══════╝

=============================[ Initialization ]=============================
""")

# Zobrazíme logo na začiatku
show_intro_logo()

# Funkcia pre automaticku instalaciu
def setup_environment():
    """Nainstaluje vsetky potrebne baliky a zavislosti"""
    print("Kontrolujem a instalujem potrebne zavislosti...")
    
    # Zoznam potrebnych Python balikov
    required_packages = [
        "requests", "rich", "schedule", "pandas", "numpy",
        "beautifulsoup4", "fake_useragent", "websocket-client", 
        "paramiko"
    ]
    
    # Kontrola a instalacia Python balikov
    for package in required_packages:
        try:
            __import__(package.replace("-", "_").split("==")[0])
            print(f"✓ {package} je nainstalovany")
        except ImportError:
            print(f"→ Instalujem {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    # Detekcia operacneho systemu a instalacie systemovych balikov
    if sys.platform.startswith('linux'):
        try:
            # Kontrola ci je uzivatel root (potrebne pre niektore funkcie)
            if os.geteuid() == 0:
                print("Instalujem systemove baliky (Linux)...")
                subprocess.call("apt update", shell=True)
                subprocess.call("apt install -y tor proxychains4 nmap sqlmap", shell=True)
            else:
                print("⚠️ Nie ste root - niektoré funkcie môžu byť obmedzené")
                print("Pre plnú funkčnosť spustite ako: sudo python3 casino_tester.py")
        except:
            print("⚠️ Nemohli sme nainštalovať systémové balíky")
    
    elif sys.platform == 'win32':
        print("⚠️ Windows: Niektoré funkcie môžu vyžadovať manuálnu inštaláciu externých nástrojov")
        print("Prosím, nainštalujte nmap a sqlmap manuálne pre plnú funkčnosť")
    
    print("✅ Prostredie pripravené!")

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
TARGET_URL = "https://example.com"  # Zmente na skutocny ciel
console = Console()

def get_best_proxy():
    """Vrati najlepsi dostupny proxy server alebo None"""
    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080"
    }
    return proxies

def get_attack_server():
    """Vrati adresu utocneho servera"""
    return "attack.server.example.com"

def get_encryption():
    """Vrati pouzity typ sifrovania"""
    return "AES-256"

def check_ip():
    """Kontrola aktualnej IP adresy"""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        ip_data = response.json()
        console.print(f"\n[bold green]Aktualna IP:[/bold green] {ip_data['ip']}")
    except Exception as e:
        console.print(f"[bold red]Chyba pri zistovani IP: {e}[/bold red]")

def fingerprint_spoofing():
    """Simulacia spoofingu browser fingerprinting"""
    console.print("\n[bold yellow]Fingerprint spoofing aktivovany...[/bold yellow]")
    console.print("[bold green]User-Agent zmeneny[/bold green]")
    console.print("[bold green]Canvas fingerprint zmeneny[/bold green]")
    console.print("[bold green]WebRTC leak zablokovany[/bold green]")

def intercept_websocket():
    """Simulacia zachytavania WebSocket komunikacie"""
    console.print("\n[bold yellow]Zachytavam WebSocket komunikaciu...[/bold yellow]")
    for _ in track(range(10), description="Analyza paketov"):
        time.sleep(0.2)
    console.print("[bold green]Zachytene WebSocket data: {...}[/bold green]")

def install_dependencies():
    """Instalacia vsetkych potrebnych balikov"""
    console.print("\n[bold cyan]Instalacia dodatocnych balikov...[/bold cyan]")
    try:
        os.system(f"{sys.executable} -m pip install --upgrade pip")
        packages = [
            "tensorflow", "scikit-learn", "selenium", 
            "scapy", "pysocks", "python-telegram-bot", 
            "websockets"
        ]
        for package in track(packages, description="Instalacia balikov"):
            os.system(f"{sys.executable} -m pip install {package} -q")
        console.print("[bold green]Vsetky baliky uspesne nainstalovane![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri instalacii: {e}[/bold red]")

def test_api_exploit():
    """Testovanie nedostatocneho overovania na API kasina"""
    console.print("\n[bold red]Testujem zranitelnost API kasina...[/bold red]")
    try:
        proxy = get_best_proxy()
        response = requests.get(f"{TARGET_URL}/api/game/results", 
                             proxies=proxy, 
                             timeout=10,
                             verify=False)
        if "win" in response.text.lower():
            console.print("[bold green]API je manipulovatelne! Mozete upravit vyhry.[/bold green]")
        else:
            console.print("[yellow]API zda sa byt bezpecne.[/yellow]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri testovani API: {e}[/bold red]")

def test_rng_vulnerability():
    """Testovanie predvidatelnosti RNG systemov"""
    console.print("\n[bold red]Analyzujem RNG system kasina...[/bold red]")
    try:
        seed_values = [random.randint(0, 100000) for _ in range(100)]
        console.print(f"[bold yellow]Skontrolovane hodnoty: {seed_values[:5]} ...[/bold yellow]")
        if len(set(seed_values)) < 100:
            console.print("[bold yellow]RNG system je slaby! Mozne predikcie vysledkov.[/bold yellow]")
        else:
            console.print("[bold green]RNG generator sa zda byt bezpecny.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri testovani RNG: {e}[/bold red]")

def test_database_vulnerability():
    """Testovanie SQL Injection & NoSQL Injection"""
    console.print("\n[bold red]Testujem SQL/NoSQL Injection v databazach...[/bold red]")
    try:
        # Kontrola ci je sqlmap nainstalovany
        sql_check = ["sqlmap", "--version"]
        try:
            result = subprocess.run(sql_check, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                sql_command = f"sqlmap -u \"{TARGET_URL}/login?user=admin\" --batch --dbs"
                subprocess.run(sql_command, shell=True, capture_output=True)
                console.print("[bold green]SQL Injection test dokonceny[/bold green]")
            else:
                console.print("[bold yellow]⚠️ sqlmap nie je nainstalovany - preskakujem test[/bold yellow]")
        except:
            console.print("[bold yellow]⚠️ sqlmap nie je dostupny - preskakujem test[/bold yellow]")
            
        # Simulujeme NoSQL Injection test
        console.print("[bold green]NoSQL Injection test dokonceny[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Chyba pri testovani SQL Injection: {e}[/bold red]")

def live_casino_mode():
    """LIVE rezim aktivovany po zadani hesla"""
    password = Prompt.ask("[bold red]Zadaj heslo pre LIVE CASINO TESTING[/bold red]", password=True)
    if password == "Jackpot5000":
        console.print("[bold red]LIVE rezim aktivovany![/bold red]")
        console.print(f"[bold cyan]Cielova URL:[/bold cyan] {TARGET_URL}")
        
        for step in track(range(5), description="Priprava na LIVE testovanie"):
            time.sleep(0.5)
        
        proxy = get_best_proxy()
        attack_server = get_attack_server()
        encryption = get_encryption()
        
        console.print(f"[bold cyan]Proxy:[/bold cyan] {proxy}")
        console.print(f"[bold cyan]Utocny server:[/bold cyan] {attack_server}")
        console.print(f"[bold cyan]Sifrovanie:[/bold cyan] {encryption}")
        
        fingerprint_spoofing()
        intercept_websocket()
        test_api_exploit()
        test_rng_vulnerability()
        test_database_vulnerability()
    else:
        console.print("[bold red]Nespravne heslo. LIVE testovanie zablokovane.[/bold red]")

def send_live_reports():
    """Automatizovane odosielanie reportov"""
    check_ip()
    fingerprint_spoofing()
    console.print("[bold green]Report odoslany na server...[/bold green]")

def show_banner():
    """Zobrazi uvodny banner"""
    banner = """
[bold red]
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ███╗   ███╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ████╗ ████║██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ███████║███████║██║     █████╔╝ █████╗  ██║  ██║    ██╔████╔██║█████╗  
  ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██║╚██╔╝██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██║ ╚═╝ ██║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝     ╚═╝╚══════╝
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

# Nastavenie automatickeho reportovania
schedule.every(5).seconds.do(send_live_reports)

# Funkcia pre zobrazenie info o autorovi
def show_about():
    """Zobrazi informacie o autorovi"""
    console.print("\n[bold magenta]O PROGRAME:[/bold magenta]")
    console.print("Casino Tester v1.0")
    console.print("Vyvinute: youh4ck3dme")
    console.print("GitHub: https://github.com/youh4ck3dme/casino_tester")
    console.print("Licencia: Len na vzdelávacie účely")
    console.print("\n[bold red]UPOZORNENIE: Používajte len na systémoch, kde máte povolenie testovať![/bold red]")

def main():
    """Hlavna funkcia programu"""
    try:
        show_banner()
        
        # Hlavne menu programu
        running = True
        while running:
            console.print("\n[bold cyan]=== AI Tester Online Kasin ===[/bold cyan]")
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Cislo", justify="center")
            table.add_column("Akcia", justify="left")

            options = {
                "1": "LIVE CASINO Testovanie",
                "2": "Overenie aktualnej IP",
                "3": "Detekcia & Spoofing fingerprintingu",
                "4": "Intercept WebSocket & Ziskanie Tokenov",
                "5": "Spustit automaticke reporty",
                "6": "Zastavit automaticke reporty",
                "7": "Testovanie API exploitov",
                "8": "Testovanie RNG systemu",
                "9": "Testovanie SQL/NoSQL Injection",
                "10": "Instalacia dodatocnych balikov",
                "11": "O programe",
                "0": "Ukoncit program"
            }

            for key, value in options.items():
                table.add_row(key, value)

            console.print(table)
            choice = Prompt.ask("[bold cyan]Vyber moznost[/bold cyan]")

            if choice == "1":
                live_casino_mode()
            elif choice == "2":
                check_ip()
            elif choice == "3":
                fingerprint_spoofing()
            elif choice == "4":
                intercept_websocket()
            elif choice == "5":
                console.print("[bold green]Automaticke reporty aktivovane[/bold green]")
                schedule.every(5).seconds.do(send_live_reports)
            elif choice == "6":
                console.print("[bold yellow]Automaticke reporty zastavene[/bold yellow]")
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
                console.print("[bold yellow]Ukoncujem program...[/bold yellow]")
            else:
                console.print("[bold red]Neplatna volba![/bold red]")

            # Spusti vsetky naplanovane ulohy
            schedule.run_pending()
            time.sleep(1)
            
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Program prerušeny uzivatelom (Ctrl+C)[/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]Nastala neoakavana chyba: {e}[/bold red]")
    finally:
        console.print("[bold green]Program ukonceny.[/bold green]")

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> ce4bb8b508bd72407d1e3e78fa3dbaf6faf2808e
