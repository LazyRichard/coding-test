from typing import *


def solution() -> None:
    a: int = int(input().strip())
    b: str = input().strip()

    i: int
    for i in range(len(b), 0, -1):
        ans: int = a * int(b[i - 1])
        print(ans)

    print(a * int(b))
