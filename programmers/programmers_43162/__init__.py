from typing import *


def solution(n: int, computers: List[List[int]]) -> int:
    remain: List[int] = [i for i in range(n)]
    num_net: int = 0

    def _net(nxt: int):
        idx: int
        conn: int
        for idx, conn in enumerate(computers[nxt]):
            if conn and idx in remain:
                remain.remove(idx)
                _net(idx)

    rc: int
    for rc in range(n):
        idx: int
        conn: int
        if rc in remain:
            _net(rc)
            num_net += 1

    return num_net
