import pathlib

import typer
import yaml

from dice_bot import bot, dice

app = typer.Typer()


@app.command()
def start(
    config_path: pathlib.Path = typer.Option(..., exists=True, dir_okay=False)
) -> None:
    with open(config_path, mode="r") as file:
        config_file = yaml.safe_load(file)
    d6 = dice.Dice(face_number=6, name="dmg", alias="d")

    config = bot.Config.parse_obj(config_file)
    client = bot.DiceBot(command_prefix=config.command_prefix)
    client.add_command(bot.customCommand(name=d6.name, alias=d6.alias, function=d6))
    client.run(config.token)


if __name__ == "__main__":
    app()
