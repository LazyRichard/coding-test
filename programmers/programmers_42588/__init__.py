from typing import *

class Tower(NamedTuple):
    idx: int
    height: int

def solution(heights: List[int]) -> List[int]:
    stk: List[Tower] = []
    answer: List[int] = []
    visible_tower: Tower = Tower(idx=0, height=0)

    for idx, height in enumerate(heights):
        tower = Tower(idx=idx + 1, height=height)

        while stk:
            if tower.height >= stk[-1].height:
                stk.pop()

            else:
                visible_tower = stk[-1]
                stk.append(tower)
                break

        if not stk:
            stk.append(tower)
            visible_tower = Tower(idx=0, height=0)

        answer.append(visible_tower.idx)

    return answer
