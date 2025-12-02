"""
Daily Snippet #002
Datum: 2025-12-02
Thema: Log-Dateien schreiben
"""
"""Logging fuer IT-Support."""
import logging

logging.basicConfig(
    filename='it_support.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_ticket(ticket_nr, problem, loesung):
    """Loggt ein Support-Ticket."""
    logging.info(f"Ticket {ticket_nr}: {problem} -> {loesung}")

if __name__ == "__main__":
    log_ticket("T-001", "WLAN geht nicht", "Passwort zurueckgesetzt")
    log_ticket("T-002", "Drucker druckt nicht", "Treiber installiert")
    print("Log geschrieben: it_support.log")

