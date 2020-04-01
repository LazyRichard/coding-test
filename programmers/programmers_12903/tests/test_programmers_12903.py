from typing import List

import pytest

from .. import solution

@pytest.mark.parametrize("a,expected", [
    ["abcde", "c"],
    ["qwer", "we"]
])
def test_solution(a: str, expected: str) -> None:
    assert solution(a) == expected
