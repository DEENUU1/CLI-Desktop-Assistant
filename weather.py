from requests import get
import json
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class WeatherData:
    """
    Dataclass for weather data
    """
    temp: float
    desc: str
    pressure: int
    wind_speed: float


class GetWeatherData:
    """
    Class for getting weather data
    """
    def __init__(self, city: str):
        self.city = city
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"

    def get_data(self) -> WeatherData:
        """
        Returns weather data
        Get data from API and parse it to JSON format
        """
        response = get(self.url)
        # handle error if city not found
        if response.status_code == 404:
            return None
        data = json.loads(response.text)

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]

        return WeatherData(temp, desc, pressure, wind_speed)
