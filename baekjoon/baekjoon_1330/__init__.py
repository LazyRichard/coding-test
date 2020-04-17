from typing import *


def solution() -> None:
    a: int
    b: int
    a, b = map(int, input().strip().split())

    if a == b:
        print("==")
    else:
        print(">" if a > b else "<")
