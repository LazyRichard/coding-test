import pytest

from .. import solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ["1S2D*3T", 37],
        ["1D2S#10S", 9],
        ["1D2S0T", 3],
        ["1S*2T*3S", 23],
        ["1D#2S*3S", 5],
        ["1T2D3D#", -4],
        ["1D2S3T*", 59],
    ],
)
def test_solution(test_input: str, expected: int) -> None:
    assert solution(test_input) == expected
