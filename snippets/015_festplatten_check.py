"""
Daily Snippet #015
Datum: 2025-12-14
Thema: Festplatten-Speicher pruefen
"""
"""Festplatten-Speicherplatz pruefen."""
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

