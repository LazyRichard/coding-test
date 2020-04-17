from typing import *


def solution() -> None:
    ins: List[str] = input().strip().split()
    num_rev: List[int] = []

    num: str
    for num in ins:
        rev: str = ""
        for i in range(len(num), 0, -1):
            rev += num[i - 1]

        num_rev.append(rev)

    print(num_rev[0] if num_rev[0] > num_rev[1] else num_rev[1])

