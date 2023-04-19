import os
import json
from requests import get 
from dataclasses import dataclass
from dotenv import load_dotenv
from rich import print


load_dotenv()

@dataclass
class NasaAPODData:
    date: str
    explanation: str
    hdurl = str
    url = str 


class NasaAPOD:
    def __init__(self):
        self.api_key = os.getenv("NASA_API_KEY")
        self.base_url = "https://api.nasa.gov/planetary/apod?api_key="
    
    def _get_nasa_image(self):
        response = get(f"{self.base_url}{self.api_key}")
        if response.status_code != 200:
            return None
        response_json = json.loads(response.text)
        return response_json
    
    def return_image_data(self):
        if self._get_nasa_image() is not None:
            data = NasaAPODData(
                date = self._get_nasa_image()["date"],
                explanation = self._get_nasa_image()["explanation"],
                # hdurl = self._get_nasa_image()["hdurl"],
                # url = self._get_nasa_image()["url"]
            )
            
            print(f"Date: {data.date} \n Explanation: {data.explanation} ")
        else:
            return "No image found" 