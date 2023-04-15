from requests import get
import json
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class WeatherData:
    temp: float
    desc: str
    pressure: int
    wind_speed: float


class GetWeatherData:
    def __init__(self, city: str):
        self.city = city
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

    def get_data(self) -> WeatherData:
        response = get(self.url)
        data = json.loads(response.text)

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]

        return WeatherData(temp, desc, pressure, wind_speed)
