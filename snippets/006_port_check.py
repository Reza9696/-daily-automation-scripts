"""
Daily Snippet #006
Datum: 2025-12-05
Thema: Port-Verbindung testen
"""
"""Port-Check - Ist ein Dienst erreichbar?"""
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

