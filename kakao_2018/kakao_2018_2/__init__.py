from typing import List
import re

def solution(dart_result: str) -> int:
    pattern: str = "(?P<score>[0-9]*)(?P<bonus>S|D|T)(?P<option>\*|\#)?"

    set_score: List[int] = [0, 0, 0]
    for i, m in enumerate(re.finditer(pattern, dart_result)):
        local_score = int(m.group("score"))

        if m.group("bonus") == "S":
            local_score = local_score ** 1
        elif m.group("bonus") == "D":
            local_score = local_score ** 2
        elif m.group("bonus") == "T":
            local_score = local_score ** 3

        if m.group("option") == "*":
            local_score *= 2

            if i > 0:
                set_score[i - 1] *= 2

        elif m.group("option") == "#":
            local_score *= -1

        set_score[i] = local_score

    return sum(set_score)
