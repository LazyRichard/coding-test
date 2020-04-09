from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize("priorities,location,expected", [
    [[2, 1, 3, 2], 2, 1],
    [[1, 1, 9, 1, 1, 1], 0, 5]
])
def test_solution(priorities: List[int], location: int, expected: int) -> None:
    assert solution(priorities, location) == expected
