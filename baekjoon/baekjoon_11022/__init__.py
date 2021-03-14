from typing import *


def solution() -> None:
    num: int = int(input().strip())

    for i in range(1, num + 1):
        a: int
        b: int
        a, b = map(int, input().strip().split())

        print("Case #{}: {} + {} = {}".format(i, a, b, a + b))
