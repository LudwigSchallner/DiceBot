"""Bot module."""
from typing import Sequence

import discord
from discord.ext.commands import Bot
import pydantic

from dice_bot.dice import Dice


class BotConfig(pydantic.BaseModel):
    """Config data for a DiceBot."""

    token: str
    command_prefix: str | Sequence[str]


class DiceConfig(pydantic.BaseModel):
    """Data for a DiceCommand."""

    name: str
    alias: str | Sequence[str]
    help_text: str
    brief_explanation: str
    dice: Dice


class Config(pydantic.BaseModel):
    """Data structure of the config file."""

    bot_config: BotConfig
    dices: Sequence[DiceConfig]


class DiceBot(Bot):
    """Data for a DiceBot."""

    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=command_prefix, intents=intents)


def custom_command(command: DiceConfig):
    """Return a bot command with the given parameters."""

    @discord.ext.commands.command(
        name=command.name,
        aliases=command.alias,
        help=command.help_text,
        brief=command.help_text,
    )
    async def _command(ctx, command_attribute: int = 1):
        await ctx.send(command.dice(command_attribute))

    return _command
