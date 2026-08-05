from datetime import date
import socket


def internet_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False


def get_next_event():
    # If there is no internet, don't show an event
    if not internet_connected():
        return {
            "name": "No upcoming event",
            "days": "--"
        }

    event_name = "Halloween"
    event_date = date(2026, 10, 31)
    today = date.today()

    days_remaining = (event_date - today).days

    return {
        "name": event_name,
        "days": days_remaining
    }