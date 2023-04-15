from requests import get
import json
from dotenv import load_dotenv
import os
from rich.table import Table
from dataclasses import dataclass
from typing import Union, List, Any, Dict

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


class RecommendationShows:
    """ This class alows to return similar movies and tv shows from the API """
    def __init__(self, query: str, show_type: str):
        self.search = Search(query, show_type)
        self.type = show_type
        self.__api_key = os.getenv("MOVIEDB_API_KEY")
        self.base_url = "https://api.themoviedb.org/3/"

    def _search_for_similar(self) -> List[Dict[str, Any]]:
        """ This method is searching for similar tv shows or movies """
        all_results = []
        response = get(
            f"{self.base_url}{self.type}/{self.search.return_id}/recommendations?api_key={self.__api_key}"
        )
        json_result = json.loads(response.content)
        all_results.extend(json_result['results'])

        return all_results

    def get_similar_shows(self) -> list[MovieData]:
        """
        This method returns title, overview, photo for all similar movies and tv shows
        """

        if self.type == "movie":
            all_movies = []
            for movie in self._search_for_similar():
                shows_data = MovieData(
                    title=movie['title'],
                    overview=movie['overview'],
                    poster=movie['poster_path'],
                    id=movie['id']
                )
                all_movies.append(shows_data)
            return all_movies

        elif self.type == 'tv':
            all_tv_shows = []
            for show in self._search_for_similar():
                show_data = MovieData(
                    title=show['name'],
                    overview=show['overview'],
                    poster=show['backdrop_path'],
                    id=show['id']
                )
                all_tv_shows.append(show_data)
            return all_tv_shows

