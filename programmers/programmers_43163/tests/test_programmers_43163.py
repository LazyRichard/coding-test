from typing import *

import pytest

from .. import solution


@pytest.mark.skip("Not implementation yet")
@pytest.mark.parametrize("begin,target,words,expected", [
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4],
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0]
])
def test_solution(begin: str, target: str, words: List[str], expected: int) -> None:
    assert solution(begin, target, words) == expected
