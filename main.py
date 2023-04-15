import typer
from rich import print


app = typer.Typer(help="This is a CLI Desktop Assistant. I hope you will like it!")


@app.command()
def main():
    print("[green]Welcome in CLI Desktop Assistant.[/green]")
    print("This is an opensource project made with Typer :rocket:")


if __name__ == "__main__":
    app()