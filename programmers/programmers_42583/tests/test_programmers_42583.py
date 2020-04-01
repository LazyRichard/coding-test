from typing import List

import pytest

from programmers_42583 import solution

@pytest.mark.parametrize("bridge_length,weight,truck_weights,expected",
[
    [2, 10, [7, 4, 5, 6], 8],
    [100, 100, [10], 101],
    [100, 100, [10,10,10,10,10,10,10,10,10,10], 110]
])
def test_solution_default_condition(bridge_length:int, weight:int, truck_weights:List[int], expected:int) -> None:
    assert solution(bridge_length, weight, truck_weights) == expected