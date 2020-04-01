from typing import List

def solution(arr: List[int], divisor: int) -> List[int]:
    answer: List[int] = []

    for ele in arr:
        if ele % divisor == 0:
            answer.append(ele)

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)
