from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize(
    "heights,expected",
    [
        [[6, 9, 5, 7, 4], [0, 0, 2, 2, 4]],
        [[3, 9, 9, 3, 5, 7, 2], [0, 0, 0, 3, 3, 3, 6]],
        [[1, 5, 3, 6, 7, 6, 5], [0, 0, 2, 0, 0, 5, 6]],
    ],
)
def test_solution(heights: List[int], expected: List[int]) -> None:
    assert solution(heights) == expected
