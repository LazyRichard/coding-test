from typing import List

import pytest

from .. import solution

@pytest.mark.parametrize("arr,expected", [
    [[1, 1, 3, 3, 0, 1, 1], [1, 3, 0, 1]],
    [[4, 4, 4, 3, 3], [4, 3]]
])
def test_solution(arr: List[int], expected: List[int]) -> None:
    assert solution(arr) == expected
