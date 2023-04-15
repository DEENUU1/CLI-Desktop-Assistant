from dotenv import load_dotenv
import os
from requests import get
import json
from dataclasses import dataclass


load_dotenv()


@dataclass
class NewsData:
    """
    Dataclass for news data
    """
    title: str
    author: str
    url: str


class GetNewsData:
    def __init__(self, country_code):
        self.country_code = country_code
        self.api_key = os.getenv("NEWS_API_KEY")
        self.url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={self.api_key}"

    def get_news(self):
        result = get(self.url)
        result_json = json.loads(result.content)
        articles = result_json["articles"]
        all_articles = []
        for article in articles:
            title = article["title"]
            author = article["author"]
            url = article["url"]

            all_articles.append(
                NewsData(title=title,
                         author=author,
                         url=url)
            )

        return all_articles
