from typing import *


def solution() -> None:
    num: int = int(input().strip())

    for _ in range(num):
        a: int
        b: int
        a, b = map(int, input().strip().split())

        print(a + b)
