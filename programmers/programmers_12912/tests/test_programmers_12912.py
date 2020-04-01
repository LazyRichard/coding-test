import pytest

from .. import solution

@pytest.mark.parametrize("a,b,expected", [
    [3, 5, 12],
    [3, 3, 3],
    [5, 3, 12]
])
def test_solution(a: int, b: int, expected: int):
    assert solution(a, b) == expected
