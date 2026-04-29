import json
import os
import urllib.parse
import urllib.request

_BASE_URL = "http://api.weatherapi.com/v1/current.json"


def _api_key() -> str:
    key = os.environ.get("WEATHER_API_KEY")
    if not key:
        raise RuntimeError("WEATHER_API_KEY environment variable is not set")
    return key


def get_weather(city: str) -> dict:
    """Fetch current weather for a city from weatherapi.com.

    Returns a dict with fields: city, country, temp_c, temp_f, condition,
    humidity, wind_kph, wind_dir, feels_like_c, feels_like_f.
    Raises RuntimeError if the request fails or the API reports an error.
    """
    params = urllib.parse.urlencode({"key": _api_key(), "q": city, "aqi": "no"})
    url = f"{_BASE_URL}?{params}"

    with urllib.request.urlopen(url, timeout=5) as response:
        data = json.loads(response.read().decode())

    location = data["location"]
    current = data["current"]

    return {
        "city": location["name"],
        "country": location["country"],
        "temp_c": current["temp_c"],
        "temp_f": current["temp_f"],
        "condition": current["condition"]["text"],
        "humidity": current["humidity"],
        "wind_kph": current["wind_kph"],
        "wind_dir": current["wind_dir"],
        "feels_like_c": current["feelslike_c"],
        "feels_like_f": current["feelslike_f"],
    }
