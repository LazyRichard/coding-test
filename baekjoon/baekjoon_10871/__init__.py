from typing import *


def solution() -> None:
    result: List[int] = []

    n: int
    x: int
    n, x = map(int, input().strip().split())

    lst: List[int] = list(map(int, input().strip().split()))

    l: int
    for l in lst:
        if l < x:
            result.append(l)

    print(" ".join(map(str, result)))
