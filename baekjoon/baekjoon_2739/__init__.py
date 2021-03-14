from typing import *


def solution() -> None:
    num: int = int(input().strip())

    list(map(lambda x: print("{} * {} = {}".format(num, x, num * x)), range(1, 10)))
