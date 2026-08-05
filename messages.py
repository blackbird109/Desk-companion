from datetime import date

def get_daily_message():
    messages = [
        "Live Laugh Love",
        "Smile :)",
        "You Got This",
        "Mistakes help us improve",
        "You can do this"
    ]

    today = date.today()
    message_number = today.timetuple().tm_yday % len(messages)

    return messages[message_number]

