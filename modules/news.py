from dotenv import load_dotenv
import os
from requests import get
import json
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table

load_dotenv()

console = Console()


@dataclass
class NewsData:
    """
    Dataclass for news data
    """
    title: str
    url: str


class GetNewsData:
    def __init__(self, country_code):
        self.country_code = country_code
        self.api_key = os.getenv("NEWS_API_KEY")
        self.url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={self.api_key}"

    def get_news(self):
        result = get(self.url)
        if result.status_code != 200:
            return None
        result_json = json.loads(result.content)
        articles = result_json["articles"]
        all_articles = []
        for article in articles:
            title = article["title"]
            url = article["url"]

            all_articles.append(
                NewsData(title=title,
                         url=url
                )
            )

        return all_articles

    def return_news(self):
        if self.get_news() is not None:
            table = Table(title=f"Popular news in {self.country_code}")
            table.add_column("Title")
            table.add_column("URL", style="cyan")
            
            for article in self.get_news():
                table.add_row(
                    article.title,
                    article.url,
                )
            return table
        else:
            return "Invalid country code"
