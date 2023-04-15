import typer
from rich import print
from weather import GetWeatherData
from rich.table import Table
from rich.console import Console

app = typer.Typer(help="This is a CLI Desktop Assistant. I hope you will like it!")
console = Console()


@app.command()
def main():
    print("[green]Welcome in CLI Desktop Assistant.[/green]")
    print("This is an opensource project made with Typer :rocket:")


@app.command()
def weather(
        city: str = typer.Option(..., help="City name"),
):
    weather_data = GetWeatherData(city)
    print(f"Right now in {city} is...")

    table = Table("name", "value")
    table.add_row("temperature", f"{weather_data.get_data().temp} °C")
    table.add_row("description", weather_data.get_data().desc)
    table.add_row("wind speed", f"{weather_data.get_data().wind_speed} m/s")
    table.add_row("pressure", f"{weather_data.get_data().pressure} hPa")
    console.print(table)


if __name__ == "__main__":
    app()