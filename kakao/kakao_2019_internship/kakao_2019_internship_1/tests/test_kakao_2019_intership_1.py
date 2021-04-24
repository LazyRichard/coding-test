from typing import List

import pytest

from .. import solution


@pytest.mark.parametrize(
    "board,moves,expected",
    [
        [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1],
            ],
            [1, 5, 3, 5, 1, 2, 1, 4],
            4,
        ]
    ],
)
def test_solution(board: List[List[int]], moves: List[int], expected: int) -> None:
    assert solution(board, moves) == expected
