from typing import *


def solution() -> None:
    num: int = int(input().strip())

    for i in range(1, num + 1):
        print("*" * i)
