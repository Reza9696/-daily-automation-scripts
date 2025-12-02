#!/usr/bin/env python3
"""
Automatischer Python Snippet Generator
IT-Support & System Administration Basics
"""

import os
import random
from datetime import datetime
from pathlib import Path

SNIPPETS_DIR = Path(__file__).parent.parent / "snippets"

SNIPPETS = [
    {
        "thema": "ping_check",
        "titel": "Netzwerk Ping Test",
        "code": '''"""Ping Test - Prüfen ob ein Computer erreichbar ist."""
import subprocess
import platform

def ping(host, anzahl=4):
    """Pingt einen Host."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    befehl = ["ping", param, str(anzahl), host]
    ergebnis = subprocess.run(befehl, capture_output=True, text=True)
    erreichbar = ergebnis.returncode == 0
    status = "erreichbar" if erreichbar else "NICHT erreichbar"
    print(f"{host}: {status}")
    return erreichbar

if __name__ == "__main__":
    ping("google.com")
    ping("8.8.8.8")
'''
    },
    {
        "thema": "ip_adresse",
        "titel": "IP-Adresse herausfinden",
        "code": '''"""IP-Adresse herausfinden."""
import socket

def get_lokale_ip():
    """Findet die lokale IP-Adresse."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Nicht gefunden"

if __name__ == "__main__":
    print(f"Hostname: {socket.gethostname()}")
    print(f"Lokale IP: {get_lokale_ip()}")
'''
    },
    {
        "thema": "port_check",
        "titel": "Port-Verbindung testen",
        "code": '''"""Port-Check - Ist ein Dienst erreichbar?"""
import socket

def teste_port(host, port, timeout=3):
    """Testet ob ein Port offen ist."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        ergebnis = sock.connect_ex((host, port))
        sock.close()
        return ergebnis == 0
    except socket.error:
        return False

def teste_standard_ports(host):
    """Testet wichtige Ports."""
    ports = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3389: "RDP"}
    print(f"Port-Scan: {host}")
    for port, name in ports.items():
        status = "OFFEN" if teste_port(host, port) else "geschlossen"
        print(f"  {port} ({name}): {status}")

if __name__ == "__main__":
    teste_standard_ports("google.com")
'''
    },
    {
        "thema": "system_info",
        "titel": "System-Informationen",
        "code": '''"""Computer-Informationen auslesen."""
import platform
import socket

def get_system_info():
    """Sammelt System-Informationen."""
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "architektur": platform.machine()
    }

if __name__ == "__main__":
    info = get_system_info()
    print("=== System Info ===")
    for key, value in info.items():
        print(f"{key}: {value}")
'''
    },
    {
        "thema": "ordner_groesse",
        "titel": "Ordner-Groesse berechnen",
        "code": '''"""Ordner-Groesse berechnen."""
import os

def ordner_groesse(pfad):
    """Berechnet Ordner-Groesse in MB."""
    gesamt = 0
    for verzeichnis, ordner, dateien in os.walk(pfad):
        for datei in dateien:
            try:
                gesamt += os.path.getsize(os.path.join(verzeichnis, datei))
            except (OSError, FileNotFoundError):
                pass
    return gesamt / (1024 * 1024)

if __name__ == "__main__":
    pfad = "."
    mb = ordner_groesse(pfad)
    print(f"Ordner: {pfad}")
    print(f"Groesse: {mb:.2f} MB")
'''
    },
    {
        "thema": "datei_suche",
        "titel": "Dateien suchen",
        "code": '''"""Dateien nach Muster suchen."""
from pathlib import Path

def suche_dateien(start_ordner, muster):
    """Sucht Dateien nach Muster."""
    start = Path(start_ordner)
    gefunden = list(start.rglob(muster))
    return gefunden

if __name__ == "__main__":
    dateien = suche_dateien(".", "*.py")
    print(f"Python-Dateien gefunden: {len(dateien)}")
    for d in dateien[:5]:
        print(f"  {d}")
'''
    },
    {
        "thema": "csv_inventar",
        "titel": "IT-Inventar mit CSV",
        "code": '''"""CSV Dateien fuer IT-Inventar."""
import csv
from datetime import datetime

def erstelle_inventar():
    """Erstellt Beispiel-Inventar."""
    inventar = [
        {"PC": "PC-001", "User": "Max", "Status": "Aktiv"},
        {"PC": "PC-002", "User": "Anna", "Status": "Aktiv"},
        {"PC": "PC-003", "User": "Lager", "Status": "Reparatur"},
    ]
    datei = f"inventar_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(datei, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["PC", "User", "Status"])
        writer.writeheader()
        writer.writerows(inventar)
    print(f"Inventar erstellt: {datei}")

if __name__ == "__main__":
    erstelle_inventar()
'''
    },
    {
        "thema": "log_schreiben",
        "titel": "Log-Dateien schreiben",
        "code": '''"""Logging fuer IT-Support."""
import logging

logging.basicConfig(
    filename='it_support.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_ticket(ticket_nr, problem, loesung):
    """Loggt ein Support-Ticket."""
    logging.info(f"Ticket {ticket_nr}: {problem} -> {loesung}")

if __name__ == "__main__":
    log_ticket("T-001", "WLAN geht nicht", "Passwort zurueckgesetzt")
    log_ticket("T-002", "Drucker druckt nicht", "Treiber installiert")
    print("Log geschrieben: it_support.log")
'''
    },
    {
        "thema": "passwort_generator",
        "titel": "Sichere Passwoerter generieren",
        "code": '''"""Passwort-Generator."""
import secrets
import string

def generiere_passwort(laenge=12):
    """Generiert sicheres Passwort."""
    zeichen = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(secrets.choice(zeichen) for _ in range(laenge))

if __name__ == "__main__":
    print("=== 5 sichere Passwoerter ===")
    for i in range(5):
        print(f"{i+1}. {generiere_passwort(14)}")
'''
    },
    {
        "thema": "dns_lookup",
        "titel": "DNS Abfrage",
        "code": '''"""DNS Abfrage - Hostname zu IP."""
import socket

def dns_lookup(hostname):
    """Wandelt Hostname in IP um."""
    try:
        ips = socket.gethostbyname_ex(hostname)[2]
        print(f"{hostname}: {', '.join(ips)}")
        return ips
    except socket.gaierror as e:
        print(f"DNS Fehler: {e}")
        return []

if __name__ == "__main__":
    dns_lookup("google.com")
    dns_lookup("microsoft.com")
'''
    },
    {
        "thema": "festplatten_check",
        "titel": "Festplatten-Speicher pruefen",
        "code": '''"""Festplatten-Speicherplatz pruefen."""
import shutil

def check_speicher(pfad="/"):
    """Prueft Speicherplatz."""
    total, used, free = shutil.disk_usage(pfad)
    gb = 1024**3
    print(f"Gesamt: {total/gb:.1f} GB")
    print(f"Benutzt: {used/gb:.1f} GB")
    print(f"Frei: {free/gb:.1f} GB ({free/total*100:.1f}%)")

if __name__ == "__main__":
    check_speicher()
'''
    },
    {
        "thema": "backup_script",
        "titel": "Einfaches Backup-Script",
        "code": '''"""Einfaches Backup-Script."""
import shutil
import os
from datetime import datetime

def backup(quell_ordner, ziel_ordner):
    """Erstellt Backup mit Datum."""
    if not os.path.exists(quell_ordner):
        print(f"Ordner nicht gefunden: {quell_ordner}")
        return
    datum = datetime.now().strftime("%Y-%m-%d_%H-%M")
    name = os.path.basename(quell_ordner)
    backup_pfad = os.path.join(ziel_ordner, f"{name}_{datum}")
    os.makedirs(ziel_ordner, exist_ok=True)
    shutil.copytree(quell_ordner, backup_pfad)
    print(f"Backup erstellt: {backup_pfad}")

if __name__ == "__main__":
    print("Beispiel: backup('C:/Projekte', 'D:/Backups')")
'''
    },
]


def get_existing_snippets():
    """Findet existierende Snippets."""
    existing = set()
    if SNIPPETS_DIR.exists():
        for file in SNIPPETS_DIR.glob("*.py"):
            parts = file.stem.split("_", 1)
            if len(parts) > 1:
                existing.add(parts[1])
    return existing


def get_next_number():
    """Naechste Snippet-Nummer."""
    if not SNIPPETS_DIR.exists():
        return 1
    max_num = 0
    for file in SNIPPETS_DIR.glob("*.py"):
        parts = file.stem.split("_", 1)
        if parts[0].isdigit():
            max_num = max(max_num, int(parts[0]))
    return max_num + 1


def generate_snippet():
    """Generiert taegliches Snippet."""
    SNIPPETS_DIR.mkdir(exist_ok=True)
    
    existing = get_existing_snippets()
    available = [s for s in SNIPPETS if s["thema"] not in existing]
    
    if not available:
        available = SNIPPETS
    
    snippet = random.choice(available)
    num = get_next_number()
    filename = f"{num:03d}_{snippet['thema']}.py"
    filepath = SNIPPETS_DIR / filename
    
    content = f'''"""
Daily Snippet #{num:03d}
Datum: {datetime.now().strftime("%Y-%m-%d")}
Thema: {snippet["titel"]}
"""
{snippet["code"]}
'''
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Erstellt: {filename}")
    return filepath


if __name__ == "__main__":
    generate_snippet()
