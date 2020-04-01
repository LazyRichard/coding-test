from typing import List, Iterable
from itertools import cycle


def solution(answers: List[int]) -> List[int]:
    patterns: List[Iterable[int]] = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    score: List[int] = [0, 0, 0]

    for i in range(len(score)):
        score[i] = sum(map(lambda x, y: x == y, patterns[i], answers))

    max_score: int = max(score)

    return sorted([(i + 1) for i, x in enumerate(score) if x == max_score])
