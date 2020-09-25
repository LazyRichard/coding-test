from typing import *


def solution(prices: List[int]) -> List[int]:
    result: List[int] = []
    idx: int = 0

    i: int
    for i in range(len(prices)):
        idx = i + 1
        price: int = prices[i]
        while idx != len(prices):
            top: int = prices[idx]
            idx += 1

            if top < price:
                break

        result.append(idx - (i + 1))

    return result
