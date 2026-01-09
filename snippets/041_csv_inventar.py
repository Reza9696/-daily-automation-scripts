"""
Daily Snippet #041
Datum: 2026-01-09
Thema: IT-Inventar mit CSV
"""
"""CSV Dateien fuer IT-Inventar."""
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

