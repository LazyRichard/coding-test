from typing import List, Set

def solution(n: int, lost: List[int], reserve: List[int]) -> int:
    reserve_set: Set[int] = set(reserve) - set(lost)
    lost_set: Set[int] = set(lost) - set(reserve)

    for rev in reserve_set:
        if rev - 1 in lost_set:
            lost_set.remove(rev - 1)
        elif rev + 1 in lost_set:
            lost_set.remove(rev + 1)

    return n - len(lost_set)
