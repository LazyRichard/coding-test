from typing import *

import itertools

def solution(nums: List[int], target: int) -> List[int]:
    answer: List[int] = []

    it = itertools.combinations(range(len(nums)), 2)
    for i in it:
        if nums[i[0]] + nums[i[1]] == target:
            return list(i)

    return answer
