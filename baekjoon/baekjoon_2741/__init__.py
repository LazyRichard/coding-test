from typing import *


def solution() -> None:
    num: int = int(input().strip())

    list(map(lambda x: print(x), range(1, num + 1)))
