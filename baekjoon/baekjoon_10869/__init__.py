from typing import *


def solution() -> None:
    a: int
    b: int

    a, b = map(int, input().strip().split())

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
