from typing import List

import pytest

from .. import solution, solution2


@pytest.mark.parametrize(
    "n,arr1,arr2,expected",
    [
        [
            5,
            [9, 20, 28, 18, 11],
            [30, 1, 21, 17, 28],
            ["#####", "# # #", "### #", "#  ##", "#####"],
        ],
        [
            6,
            [46, 33, 33, 22, 31, 50],
            [27, 56, 19, 14, 14, 10],
            ["######", "###  #", "##  ##", " #### ", " #####", "### # "],
        ],
    ],
)
def test_solution(
    n: int, arr1: List[int], arr2: List[int], expected: List[str]
) -> None:
    assert solution(n, arr1, arr2) == expected
    assert solution2(n, arr1, arr2) == expected
