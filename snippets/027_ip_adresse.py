"""
Daily Snippet #027
Datum: 2025-12-26
Thema: IP-Adresse herausfinden
"""
"""IP-Adresse herausfinden."""
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

