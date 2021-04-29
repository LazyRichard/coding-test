from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize("nums,target,expected", [
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]]
])
def test_solution(nums: List[int], target: int, expected: List[int]) -> None:
    assert solution(nums, target) == expected
