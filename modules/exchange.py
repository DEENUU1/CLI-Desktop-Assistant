from requests import get
from dataclasses import dataclass
from rich.table import Table
import json 


@dataclass
class ExchangeRate:
    rate: float
    currency: str


class GetExchangeRates:
    def __init__(self, code: str):
        self.code = code
        self.url = f"https://api.nbp.pl/api/exchangerates/rates/A/{self.code}/?format=json"

    def _get_single_exchange_rate(self) -> ExchangeRate | None:
        response = get(self.url)
        if response.status_code != 200:
            return None
        data = response.json()
        return ExchangeRate(rate=data["rates"][0]["mid"], currency=data["currency"])

    def return_exchange_rate(self):
        if self._get_single_exchange_rate() is not None:
            table = Table("code", "name", "rate")
            table.add_row(self.code, self._get_single_exchange_rate().currency, str(self._get_single_exchange_rate().rate))
            return table
        else:
            return "Invalid token"


class GetListOfExchangeRates:
    def __init__(self):
        self.url = f"https://api.nbp.pl/api/exchangerates/tables/a/?format=json"

    def _search_for_rates(self):
        all_results = []
        response = get(self.url)
        if response.status_code != 200:
            return None
        json_result = json.loads(response.content)
        all_results.extend(json_result[0]["rates"])
        return all_results
    
    def _get_exchange_rate(self):
        all_results = []
        for data in self._search_for_rates():
            exchange_data = ExchangeRate(
                rate=data["mid"],
                currency=data["code"]
            ) 
            all_results.append(exchange_data)
        return all_results
    
    def return_exchange_rate(self):
        if self._get_exchange_rate() is not None:
            table = Table("code", "rate")
            for data in self._get_exchange_rate():
                table.add_row(
                    data.currency, 
                    str(data.rate)
                )
            return table
        else:
            return "No exchange rate found"

