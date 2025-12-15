"""
Daily Snippet #016
Datum: 2025-12-15
Thema: Netzwerk Ping Test
"""
"""Ping Test - Prüfen ob ein Computer erreichbar ist."""
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

