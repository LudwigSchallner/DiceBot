import pathlib

import typer
import yaml

from dice_bot import bot

app = typer.Typer()


@app.command()
def start(
    config_path: pathlib.Path = typer.Option(..., exists=True, dir_okay=False)
) -> None:
    """Entry point for starting the server and initializing the given config."""
    with open(config_path, mode="r") as file:
        config_file = yaml.safe_load(file)

    config = bot.Config.parse_obj(config_file)
    bot_config = config.bot_config
    dices = config.dices

    client = bot.DiceBot(command_prefix=bot_config.command_prefix)

    for dice_command in dices:
        client.add_command(bot.custom_command(dice_command))

    client.run(bot_config.token)


if __name__ == "__main__":
    app()
