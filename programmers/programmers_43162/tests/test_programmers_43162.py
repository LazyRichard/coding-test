from typing import List

import pytest

from .. import solution


@pytest.mark.parametrize(
    "n,computers,expected",
    [
        [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2],
        [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1],
    ],
)
def test_solution(n: int, computers: List[List[int]], expected: int):
    assert solution(n, computers) == expected
