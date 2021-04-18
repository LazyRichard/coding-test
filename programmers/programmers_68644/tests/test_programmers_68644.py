from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize(
    "numbers,expected",
    [[[2, 1, 3, 4, 1], [2, 3, 4, 5, 6, 7]], [[5, 0, 2, 7], [2, 5, 7, 9, 12]]],
)
def test_solution(numbers: List[int], expected: List[int]) -> None:
    assert solution(numbers) == expected
