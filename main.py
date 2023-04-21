import typer
from rich import print
from modules.weather import GetWeatherData
from rich.console import Console
from modules.news import GetNewsData
from modules.exchange import GetExchangeRates, GetListOfExchangeRates
from modules.movies import RecommendationShows, MovieTrailers, Search
from modules.quotes import RandomQuotes
from modules.nasa import NasaAPOD
from modules.youtube import YoutubeDownloader
from modules.computer import return_pc_info


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

@app.command(help="Return exchange rates list")
def currency_list():
    currency_data = GetListOfExchangeRates()
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


@app.command(help="Returns a random quote")
def quote():
    quote_data = RandomQuotes()
    console.print(f'"{quote_data.return_random_quote()[0]}"',
                  "~~", quote_data.return_random_quote()[1] )

@app.command(help="Returns NASA APOD")
def nasa():
    nasa_image = NasaAPOD()
    console.print(nasa_image.return_image_data())

@app.command(help="Download youtube video or song")
def youtube_downloader(
    url: str = typer.Option(..., help="Youtube url"),
    type: str = typer.Option(..., help="Type of download video or audio"),
):
    downloader = YoutubeDownloader(url)
    console.print(downloader.download_file(type))

@app.command(help="Return youtube video thumbnail")
def youtube_thumbnail(
    url: str = typer.Option(..., help="Youtube url"),
):
    thumbnail = YoutubeDownloader(url).return_video_thumbnail()
    console.print(thumbnail)

@app.command(help="Return computer info")
def pc():
    console.print(return_pc_info())
    

if __name__ == "__main__":
    app()

