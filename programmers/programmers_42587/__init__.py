from typing import *

from collections import deque

def solution(priorities: List[int], location: int) -> int:
    que: deque = deque(priorities)
    print_cnt: int = 0

    while que:
        ele: int = que.popleft()
        location -= 1

        if any(map(lambda x: x > ele, que)):
            que.append(ele)

            if location < 0:
                location += len(que)

        else:
            print_cnt += 1

            if location < 0:
                break

    return print_cnt
