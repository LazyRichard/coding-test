from __future__ import annotations
from typing import *

class TowerInfo(NamedTuple):
    idx: int
    height: int

def solution() -> None:
    n: int = int(input().strip())
    first_seen: List[int] = []
    stk: List[TowerInfo] = []

    visible_tower: TowerInfo = TowerInfo(idx=0, height=0)
    for idx, th in enumerate(map(int, input().strip().split())):
        tower: TowerInfo = TowerInfo(idx=idx + 1, height=th)

        while stk:
            if tower.height > stk[-1].height:
                stk.pop()

            else:
                visible_tower = stk[-1]
                stk.append(tower)
                break

        if not stk:
            stk.append(tower)
            visible_tower = TowerInfo(idx=0, height=0)

        first_seen.append(visible_tower.idx)

    print(" ".join(map(str, first_seen)))
