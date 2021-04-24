from kakao_1 import solution

import pytest

@pytest.mark.parametrize("test_input,expected", [
    ["a", 1],
    ["aabbaccc", 7],
    ["ababcdcdababcdcd", 9],
    ["abcabcdede", 8],
    ["abcabcabcabcdededededede", 14],
    ["xababcdcdababcdcd", 17]
])
def test_kakao_1(test_input: str, expected: int):
    assert solution(test_input) == expected
