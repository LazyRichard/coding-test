from typing import List

import pytest

from .. import solution

@pytest.mark.parametrize("n,lost,reserve,expected", [
    [5, [2, 4], [1, 3, 5], 5],
    [5, [2, 4], [3], 4],
    [3, [3], [1], 2],
    [5, [1, 2, 3, 4, 5], [1], 1],
    [5, [1], [1], 5],
    [15, [1, 2, 3], [1, 2, 3], 15]
])
def test_solution(n: int, lost: List[int], reserve: List[int], expected: int):
    assert solution(n, lost, reserve) == expected
