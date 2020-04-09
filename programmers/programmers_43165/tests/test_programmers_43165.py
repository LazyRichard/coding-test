from typing import List

import pytest

from .. import solution


@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        [[1, 1, 1, 1, 1], 3, 5],
        [[1, 2, 3], 0, 2],
    ],
)
def test_solution(numbers: List[int], target: int, expected: int) -> None:
    assert solution(numbers, target) == expected
