"""Dice module."""
import random
from typing import Mapping, Sequence

import pydantic


class Dice(pydantic.BaseModel):
    """Dice BaseModel"""

    face_number: int
    command: str
    result_to_text: Mapping[int, str] = {}
    sum_up: bool = False

    def _roll_dice(self) -> int:
        """Roll a 'number' dice."""
        return random.randint(0, self.face_number)


class Dices(Dice):
    """Data of multiple dices."""

    dices: Sequence[Dice]
