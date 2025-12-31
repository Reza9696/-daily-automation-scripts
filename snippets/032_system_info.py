"""
Daily Snippet #032
Datum: 2025-12-31
Thema: System-Informationen
"""
"""Computer-Informationen auslesen."""
import platform
import socket

def get_system_info():
    """Sammelt System-Informationen."""
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "architektur": platform.machine()
    }

if __name__ == "__main__":
    info = get_system_info()
    print("=== System Info ===")
    for key, value in info.items():
        print(f"{key}: {value}")

