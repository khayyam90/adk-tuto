import urllib.request
import json

_IP_API_URL = "http://ip-api.com/json/"


def get_location() -> dict:
    """Fetch location data for the current public IP from ip-api.com.

    Returns a dict with fields like city, regionName, country, lat, lon, etc.
    Raises RuntimeError if the request fails or the API reports an error.
    """
    with urllib.request.urlopen(_IP_API_URL, timeout=5) as response:
        data = json.loads(response.read().decode())

    if data.get("status") != "success":
        raise RuntimeError(f"ip-api.com error: {data.get('message', 'unknown error')}")

    return data


def get_current_city() -> str:
    """Return the city name inferred from the current public IP address."""
    return get_location()["city"]
