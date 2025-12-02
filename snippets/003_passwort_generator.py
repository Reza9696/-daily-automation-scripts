"""
Daily Snippet #003
Datum: 2025-12-02
Thema: Sichere Passwoerter generieren
"""
"""Passwort-Generator."""
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

