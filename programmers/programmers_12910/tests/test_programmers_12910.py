from typing import List

import pytest

from programmers_12910 import solution

@pytest.mark.parametrize("arr,divisor,expected", [
    [[5, 9, 7, 10], 5, [5, 10]],
    [[2, 36, 1, 3], 1, [1, 2, 3, 36]],
    [[3, 2, 6], 10, [-1]]
])
def test_solution(arr: List[int], divisor: int, expected: List[int]):
    assert solution(arr, divisor) == expected
