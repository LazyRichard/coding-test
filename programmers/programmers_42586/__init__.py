from typing import *
import math
from collections import deque
import operator


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    results: List[int] = []
    idx: int = 0

    new_progresses: Deque[int] = deque(progresses)
    new_speeds: Deque[int] = deque(speeds)
    while len(new_progresses):
        release: List[int] = []

        speed: int = new_speeds[0]
        progress: int = new_progresses[0]

        min_days: int = int(math.ceil((100 - progress) / speed))

        applied_speeds: List[int] = list(map(lambda x: x * min_days, new_speeds))
        new_progresses = deque(map(operator.add, new_progresses, applied_speeds))

        for i in range(len(new_progresses)):
            if new_progresses[i] >= 100:
                release.append(new_progresses[i])
            else:
                break

        results.append(len(release))

        for i in range(len(release)):
            new_progresses.popleft()
            new_speeds.popleft()

    return results
