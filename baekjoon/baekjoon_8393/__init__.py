from typing import *


def solution() -> None:
    result: int = 0

    num: int = int(input().strip())

    i: int
    for i in range(1, num + 1):
        result += i

    print(result)
