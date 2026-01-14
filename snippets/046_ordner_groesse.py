"""
Daily Snippet #046
Datum: 2026-01-14
Thema: Ordner-Groesse berechnen
"""
"""Ordner-Groesse berechnen."""
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

