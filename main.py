import typer
from rich import print
from modules.weather import GetWeatherData
from rich.console import Console
from modules.news import GetNewsData
from modules.exchange import GetExchangeRates
from modules.movies import RecommendationShows, MovieTrailers, Search


app = typer.Typer(
    name="Desktop Assistant CLI",
    add_completion=False,
    rich_markup_mode="rich",
    help="📕[bold green] Welcome in CLI Desktop Assistant. CLI.[/bold green]"
         "This is a CLI Desktop Assistant made with Typer",
)

console = Console()


@app.command(help="Returns a current weather in a given city")
def weather(
    city: str = typer.Option(..., help="City name"),
):
    weather_data = GetWeatherData(city)
    print(f"Right now in {city} is...")
    console.print(weather_data.return_data())


@app.command(help="Returns a news in a given country")
def news(
    country_code: str = typer.Option(..., help="Country code"),
):
    news_data = GetNewsData(country_code)
    console.print(news_data.return_news())


@app.command(help="Returns a currency exchange rate")
def currency(
    currency_code: str = typer.Option(..., help="Currency code"),
):
    currency_data = GetExchangeRates(currency_code)
    console.print(currency_data.return_exchange_rate())


@app.command(help="Returns a movie and tv series recommendation")
def show(
    title: str = typer.Option(..., help="Movie title"),
    show_type: str = typer.Option(..., help="Show type"),
):
    show_data = RecommendationShows(title, show_type)
    console.print(show_data.return_show_data())


@app.command(help="Returns a movie trailer")
def trailers(
    id: int = typer.Option(..., help="Show id"),
):
    trailer_data = MovieTrailers(id)
    console.print(trailer_data.return_trailers())


@app.command(help="Returns a show ID from themoviedb API")
def show_id(
    title: str = typer.Option(..., help="Show title"),
    show_type: str = typer.Option(..., help="Show type"),
):
    show_data = Search(title, show_type)
    console.print(show_data._return_id)



if __name__ == "__main__":
    app()

