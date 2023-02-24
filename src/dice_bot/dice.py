"""Dice module."""
import random
from typing import Mapping, Sequence

import pydantic


class Dice(pydantic.BaseModel):
    """Dice BaseModel"""

    face_number: int

    def _roll(self) -> int:
        """Roll `face_number` dice."""
        return random.randint(1, self.face_number)


class ClassicDice(Dice):
    """ClassicDice with will may will be rolled multiple times."""

    def __call__(self, count) -> int:
        """Roll `count`number of `face_number` dices."""
        rolls = [self._roll() for _ in range(count)]
        return self._format(rolls)

    def _format(self, rolls: Sequence[int]) -> str:
        result_text = ", ".join(str(roll) for roll in rolls)
        return result_text


class MappingDice(Dice):
    """Dice with has a roll to text mapping."""

    result_to_text: Mapping[int, str]

    def __call__(self, count):
        rolls = [self._roll() for _ in range(count)]
        return self._map_result(rolls)

    def _map_result(self, rolls: Sequence[int]) -> str:
        rolls_as_text_list = [self.result_to_text[roll] for roll in rolls]
        return ", ".join(rolls_as_text_list)


class SortDice(ClassicDice):
    """Dice which result will be sorted."""

    def _format(self, rolls: Sequence[int]) -> str:
        rolls = rolls.sort()
        return super()._format(rolls)


class SumUpDice(ClassicDice):
    """Dice which result will be summed up."""

    def _format(self, rolls: Sequence[int]) -> str:
        without_sum = super()._format(rolls)
        return f"{without_sum} [{sum(rolls)}]"


class SucessDice(Dice):
    """Dice with is based on Success behavior."""

    threshold: int
