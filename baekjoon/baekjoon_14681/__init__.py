from typing import *


def solution() -> None:
    x: int = int(input().strip())
    y: int = int(input().strip())

    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    else:
        print("4")
