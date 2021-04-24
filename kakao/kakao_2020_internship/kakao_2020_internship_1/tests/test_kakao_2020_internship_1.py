from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize(
    "numbers,hand,expected",
    [[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"]],
)
def test_solution(numbers: List[int], hand: str, expected: int) -> None:
    assert solution(numbers, hand) == expected
