from typing import List

import pytest

from .. import solution

@pytest.mark.parametrize("test_input,expected", [
    [["119", "97674223", "1195524421"], False],
    [["123","456","789"], True],
    [["12","123","1235","567","88"], False]
])
def test_solution(test_input: List[str], expected: bool):
    assert solution(test_input) == expected