from datetime import date

def get_next_event():
    event_name = "🎃 Halloween"
    event_date = date(2026, 10, 31)
    today = date.today()

    days_remaining = (event_date - today).days

    return {
        "name": event_name,
        "days": days_remaining
    }
