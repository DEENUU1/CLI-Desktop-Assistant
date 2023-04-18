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
    release_date: str


@dataclass
class MovieTrailersData:
    name: str 
    key: str 


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
    def _return_id(self) -> Union[str, None]:
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
    """
    This class allows to return similar movies and tv shows from the API
    """

    def __init__(self, query: str, show_type: str):
        self.search = Search(query, show_type)
        self.type = show_type
        self.__api_key = os.getenv("MOVIE_API_KEY")
        self.base_url = "https://api.themoviedb.org/3/"

    def _search_for_similar(self) -> List[Dict[str, Any]] | None:
        """
        This method is searching for similar tv shows or movies
        """
        all_results = []
        response = get(
            f"{self.base_url}{self.type}/{self.search._return_id}/recommendations?api_key={self.__api_key}"
        )
        if response.status_code != 200:
            return None
        json_result = json.loads(response.content)
        all_results.extend(json_result['results'])

        return all_results

    def _get_similar_shows(self) -> list[MovieData]:
        """
        This method returns title, overview, photo for all similar movies and tv shows
        """

        if self.type == "movie":
            all_movies = []
            for movie in self._search_for_similar():
                shows_data = MovieData(
                    title=movie['title'],
                    poster=movie['poster_path'],
                    id=movie['id'],
                    release_date=movie['release_date']
                )
                all_movies.append(shows_data)
            return all_movies

        elif self.type == 'tv':
            all_tv_shows = []
            for show in self._search_for_similar():
                show_data = MovieData(
                    title=show['name'],
                    poster=show['backdrop_path'],
                    id=show['id'],
                    release_date=show['first_air_date']
                )
                all_tv_shows.append(show_data)
            return all_tv_shows

    def return_show_data(self):
        if self._get_similar_shows() is not None:
            table = Table("title", "release_date", "poster")
            for data in self._get_similar_shows():
                table.add_row(
                    str(data.id),
                    data.title,
                    data.release_date,
                    f"https://image.tmdb.org/t/p/original{data.poster}"
                )
            return table
        else:
            return "Invalid movie title"


class MovieTrailers:
    def __init__(self, id: int):
        self.api_key = os.getenv("MOVIE_API_KEY")
        self.id = id
        self.base_url = "https://api.themoviedb.org/3/movie/"
        self.youtube_url = "https://www.youtube.com/watch?v="
    
    def _search_for_trailer(self):
        all_results = []
        response = get(
            f"{self.base_url}{self.id}/videos?api_key={self.api_key}"
        )
        if response.status_code != 200:
            return None
        json_result = json.loads(response.content)
        all_results.extend(json_result['results'])
        return all_results

    def _get_trailers_data(self):
        all_trailers = []
        for trailer in self._search_for_trailer():
            trailer_data = MovieTrailersData(
                name=trailer['name'],
                key=trailer['key']
            )
            all_trailers.append(trailer_data)
        return all_trailers
    
    def return_trailers(self):
        if self._get_trailers_data() is not None:
            table = Table("name", "key")
            for data in self._get_trailers_data():
                table.add_row(
                    data.name,
                    self.youtube_url + data.key
                )
            return table
        else:
            return "Invalid movie title"
        
        