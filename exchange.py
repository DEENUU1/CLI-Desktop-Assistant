from requests import get
from dataclasses import dataclass
from rich.table import Table


@dataclass
class ExchangeRate:
    rate: float
    currency: str


class GetExchangeRates:
    def __init__(self, code: str):
        self.code = code
        self.url = f"https://api.nbp.pl/api/exchangerates/rates/A/{self.code}/?format=json"

    def get_exchange_rate(self) -> ExchangeRate | str:
        response = get(self.url)
        if response.status_code != 200:
            return "Invalid code"
        data = response.json()
        return ExchangeRate(rate=data["rates"][0]["mid"], currency=data["currency"])

    def return_exchange_rate(self):
        table = Table("code", "name", "rate")
        table.add_row(self.code, self.get_exchange_rate().currency, str(self.get_exchange_rate().rate))
        return table
