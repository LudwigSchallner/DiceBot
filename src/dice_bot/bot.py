"""Bot module."""
from typing import Sequence

import discord
from discord.ext.commands import Bot
import pydantic


class DiceBot(Bot):
    """Data for a DiceBot."""

    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=command_prefix, intents=intents)


def customCommand(name, alias, function):
    @discord.ext.commands.command(
        name=name, alias=alias, help="helpful text", brief="Brief explanation"
    )
    async def command(ctx, command):
        await ctx.send("hello world!")

    return command


class Config(pydantic.BaseModel):
    """Config data for a DiceBot."""

    token: str
    command_prefix: str | Sequence[str]
