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
        rolls = [self._roll() for _ in range(count)]
        if self.result_to_text:
            return self._map_result(rolls)
        return self._format(rolls)

    def _format(self, rolls: Sequence[int]) -> str:
        if self.sort:
            rolls = rolls.sort()
        result_text = ", ".join(rolls)
        if self.sum_up and len(rolls) > 1:
            result_sum = sum(rolls)
            result_text += f" [{result_sum}]"
        return result_text

    def _map_result(self, rolls: Sequence[int]) -> str:
        rolls_as_text_list = [self.result_to_text[roll] for roll in rolls]
        return ", ".join(rolls_as_text_list)

    def _roll(self) -> int:
        """Roll `face_number` dice."""
        return random.randint(1, self.face_number)
