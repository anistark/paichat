import typer
from paichat.prompt import start_chat

app = typer.Typer(add_completion=False)


@app.command()
def start():
    start_chat()


if __name__ == "__main__":
    app()
