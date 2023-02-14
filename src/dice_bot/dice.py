import random
from typing import Mapping, Sequence

import pydantic


class Dice(pydantic.BaseModel):
    """Dice BaseModel"""

    number: int
    command: str
    result_to_text: Mapping[int, str] = {}

    def _roll_dice(self) -> int:
        """Roll a 'number' dice."""
        return random.randint(0, self.number)


class Dices(Dice):
    dices: Sequence[Dice]
