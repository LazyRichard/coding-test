from typing import *

import itertools


def solution(numbers: List[int]) -> List[int]:
    ans: List[int] = []

    possible_combinations = itertools.combinations(numbers, 2)
    for comb in possible_combinations:
        ans.append(sum(comb))

    return sorted(list(set(ans)))
