from typing import *
from collections import Counter

def solution() -> None:
    cnt: Counter = Counter(input().strip().upper())

    max_val: int = max(cnt.values())

    if len(list(filter(lambda x: x == max(cnt.values()), cnt.values()))) > 1:
        print("?")
    else:
        print(max(cnt, key=cnt.get))
