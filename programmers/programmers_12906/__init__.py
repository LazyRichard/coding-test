from typing import List, Optional

def solution(arr: List[int]) -> List[int]:
    prev_ele: Optional[int] = None
    answer: List[int] = []

    ele: int
    for ele in arr:
        if prev_ele == ele:
            continue

        prev_ele = ele
        answer.append(ele)

    return answer

