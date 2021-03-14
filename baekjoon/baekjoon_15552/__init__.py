from typing import *
import sys


def solution() -> None:
    num: int = int(sys.stdin.readline().strip())

    for _ in range(num):
        a: int
        b: int
        a, b = map(int, sys.stdin.readline().strip().split())

        print(a + b)
