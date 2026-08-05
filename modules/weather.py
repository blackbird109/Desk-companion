# weather.py — Builder Guide 001

import requests

LOCATION = "Canton MA"
WEATHER_URL = "https://wttr.in/{location}"
TIMEOUT_SECONDS = 10


def get_weather():
    """Return current weather in the format main.py expects."""

    try:
        response = requests.get(
            WEATHER_URL.format(location=LOCATION),
            params={"format": "j1"},
            timeout=TIMEOUT_SECONDS,
            headers={"User-Agent": "DeskCompanion/1.0"},
        )

        response.raise_for_status()

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_F"]
        condition = current["weatherDesc"][0]["value"]

        return {
            "temperature": f"{temperature}°F",
            "condition": condition,
        }

    except (
        requests.RequestException,
        KeyError,
        IndexError,
        TypeError,
        ValueError,
    ):
        return {
            "temperature": "--°F",
            "condition": "Weather unavailable",
        }