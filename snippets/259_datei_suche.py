"""
Daily Snippet #259
Datum: 2026-08-16
Thema: Dateien suchen
"""
"""Dateien nach Muster suchen."""
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

