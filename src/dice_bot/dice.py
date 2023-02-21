"""Dice module."""
import random
from typing import Mapping, Sequence

import pydantic


class Dice(pydantic.BaseModel):
    """Dice BaseModel"""

    face_number: int
    result_to_text: Mapping[int, str] = {}
    sum_up: bool = False
    sort: bool = False

    def __call__(self, count=1) -> int:
        """Roll `count`number of `face_number` dices."""
        return [self._roll() for _ in range(count)]

    def _roll(self) -> int:
        """Roll `face_number` dice."""
        return random.randint(1, self.face_number)


class Dices(Dice):
    """Data of multiple dices."""

    dices: Sequence[Dice]
