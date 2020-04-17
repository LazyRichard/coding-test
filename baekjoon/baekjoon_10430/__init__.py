from typing import *


def solution() -> None:
    a: int
    b: int
    c: int

    a, b, c = map(int, input().strip().split())

    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) %c)
