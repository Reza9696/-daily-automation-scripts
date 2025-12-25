"""
Daily Snippet #026
Datum: 2025-12-25
Thema: Einfaches Backup-Script
"""
"""Einfaches Backup-Script."""
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

