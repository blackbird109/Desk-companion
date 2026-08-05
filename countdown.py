from datetime import date
import socket

print("Loading countdown.py")

def internet_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        print("Internet: YES")
        return True
    except OSError:
        print("Internet: NO")
        return False


def get_next_event():
    if not internet_connected():
        return {
            "name": "No upcoming event",
            "days": "--"
        }

    event_name = "🎃 Halloween"
    event_date = date(2026, 10, 31)

    days_remaining = (event_date - date.today()).days

    return {
        "name": event_name,
        "days": days_remaining
    }