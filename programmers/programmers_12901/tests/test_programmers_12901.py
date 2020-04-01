from typing import List

import pytest

from .. import solution

@pytest.mark.parametrize("a,b,expected", [
    [5, 24, "TUE"]
])
def test_solution(a: int, b: int, expected: str) -> None:
    assert solution(a, b) == expected
