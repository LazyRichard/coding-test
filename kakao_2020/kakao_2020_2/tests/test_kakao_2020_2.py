from typing import *

import pytest

from .. import solution


@pytest.mark.parametrize(
    "p,expected",
    [
        ["(()())()", "(()())()"],
        [")(", "()"],
        ["()))((()", "()(())()"],
        [")()()()(", "(((())))"],
    ],
)
def test_solution(p: str, expected: str) -> None:
    assert solution(p) == expected
