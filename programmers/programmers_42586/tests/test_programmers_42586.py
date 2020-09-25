from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize(
    "progresses,speeds,expected",
    [
        [[93, 30, 55], [1, 30, 5], [2, 1]],
        [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1], [1, 3, 2]],
        [[40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7], [1, 2, 3]],
        [[93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 40, 65], [2, 4]],
    ],
)
def test_solution(
    progresses: List[int], speeds: List[int], expected: List[int]
) -> None:
    assert solution(progresses, speeds) == expected
