import requests
import yaml
from pathlib import Path

from website import PROJECT_ROOT

ASSITANT_PATH = Path(__file__).parent


def get_country_json(country: str, temp_scale: str = "metric"):
    country_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={country}&units={temp_scale}&APPID={api_key()}"
    )
    return country_data.json()


def api_key():
    with open(PROJECT_ROOT / ".api_keys.yaml", "r") as file:
        return yaml.safe_load(file)["open_weather"]


def get_weather(country: str, temp_scale: str) -> str:
    emojis = {
        "clear": "☀️",
        "rain": "🌧️",
        "thunderstorm": "⛈️",
        "cloudy": "☁️",
        "snow": "❄️",
    }

    api_temp_scale = {"c": "metric", "f": "imperial"}

    weather_json = get_country_json(country, api_temp_scale[temp_scale])
    if weather_json == {"cod": "404", "message": "country not found"}:
        return "no weather information to show."
    else:
        weather = weather_json["weather"][0]["main"].lower()
        if weather == "clouds":
            weather = "cloudy"
        emoji = emojis[weather]

        temperature = weather_json["main"]["temp"]
        temp_low = weather_json["main"]["temp_min"]
        temp_high = weather_json["main"]["temp_max"]
        country_name = weather_json["name"]

        temp_symbols = {"c": "°C", "f": "°F"}
        temp_symbol = temp_symbols[temp_scale]

        return (
            f"The weather in {country_name.title()} is {weather} {emoji} - "
            f"{temperature}{temp_symbol} "
            f"(high: {temp_high}{temp_symbol} / low: {temp_low}{temp_symbol})"
        )
