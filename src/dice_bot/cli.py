import pathlib

import typer
import yaml

from dice_bot import bot

app = typer.Typer()


@app.command()
def start(
    config_path: pathlib.Path = typer.Option(..., exists=True, dir_okay=False)
) -> None:
    with open(config_path, mode="r") as file:
        config_file = yaml.safe_load(file)
    config = bot.Config.parse_obj(config_file)
    client = bot.DiceBot(command_prefix=config.command_prefix)
    client.add_command(bot.customCommand(name="name", alias="test"))
    client.run(config.token)


if __name__ == "__main__":
    app()
