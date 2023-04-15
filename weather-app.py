from requests import get
import json
from dataclasses import dataclass
import os
from dotenv import load_dotenv

@dataclass
class WeatherData:
    temp: float
    desc: str
    pressure: int
    wind_speed: float



