from typing import List

import pytest

from .. import solution


@pytest.mark.parametrize(
    "answer,expected", [
        [[1, 2, 3, 4, 5], [1]],
        [[1, 3, 2, 4, 2], [1, 2, 3]]
    ]
)
def test_solution(answer: List[int], expected: List[int]):
    assert solution(answer) == expected
