from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize(
    "prices,expected",
    [[[1, 2, 3, 2, 3], [4, 3, 1, 1, 0]], [[5, 4, 3, 5, 6, 5], [1, 1, 3, 2, 1, 0]]],
)
def test_solution(prices: List[int], expected: int) -> None:
    assert solution(prices) == expected
