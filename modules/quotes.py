import json 
from requests import get 


class RandomQuotes:
    def __init__(self):
        self.url = "https://zenquotes.io/api/random"
    
    def _get_random_quote(self):
        response = get(
            self.url
        )
        if response.status_code != 200:
            return None
        json_result = json.loads(response.content)
        return json_result[0]
    
    def return_random_quote(self):
        if self._get_random_quote() is not None:
            quote = self._get_random_quote().get('q')
            author = self._get_random_quote().get('a')
            return (quote, author)
        else:
            return "No quote found"