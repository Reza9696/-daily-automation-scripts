"""
Daily Snippet #012
Datum: 2025-12-11
Thema: DNS Abfrage
"""
"""DNS Abfrage - Hostname zu IP."""
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

