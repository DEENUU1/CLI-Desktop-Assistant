from requests import get
import json
from dotenv import load_dotenv
import os
from rich.table import Table
from dataclasses import dataclass
from typing import Union

load_dotenv()


@dataclass
class MovieData:
    id: int
    title: str
    poster: str
    overview: str


class Search:
    """ This class allows to get movie ID """

    def __init__(self, query: str, show_type: str):
        self.__api_key = os.getenv('MOVIE_API_KEY')
        self.query = query
        self.type = show_type

    def _create_query(self) -> str:
        """ This method format the user input into query """
        query_list = self.query.lower().split()
        return '-'.join(query_list)

    @property
    def return_id(self) -> Union[str, None]:
        """ This method returns user movie ID """
        base_url = f"https://api.themoviedb.org/3/search/{self.type}?api_key="
        result = get(base_url + self.__api_key + "&query=" + self._create_query())
        json_result = json.loads(result.content)
        data = json_result['results']

        if result.status_code == 200:
            try:
                return str(data[0]['id'])
            except KeyError:
                return "None"
        else:
            raise Exception(f"Status code {result.status_code}")