from requests import get
import json
from dataclasses import dataclass
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

load_dotenv()

console = Console()

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

    def get_data(self) -> None | WeatherData:
        """
        Returns weather data
        Get data from API and parse it to JSON format
        """
        response = get(self.url)
        if response.status_code == 404:
            return None
        data = json.loads(response.text)

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]

        return WeatherData(temp, desc, pressure, wind_speed)

    def return_data(self) -> Table | str:
        """
        Returns weather data
        Get data from API and parse it to JSON format
        """
        if self.get_data() is None:
            return "Invalid city name. Please try again"
        table = Table("name", "value")
        table.add_row("temperature", f"{self.get_data().temp} °C")
        table.add_row("description", self.get_data().desc)
        table.add_row("wind speed", f"{self.get_data().wind_speed} m/s")
        table.add_row("pressure", f"{self.get_data().pressure} hPa")
        return table
