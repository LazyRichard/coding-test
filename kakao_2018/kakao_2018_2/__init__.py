from typing import List
import re

BONUS_MAP = { "S": 1, "D": 2, "T": 3 }

def solution(dart_result: str) -> int:
    pattern: str = "(?P<score>[0-9]*)(?P<bonus>S|D|T)(?P<option>\*|\#)?"

    set_score: List[int] = [0, 0, 0]
    for i, m in enumerate(re.finditer(pattern, dart_result)):
        local_score = int(m.group("score"))

        local_score = local_score ** BONUS_MAP[m.group("bonus")]

        if m.group("option") == "*":
            local_score *= 2

            if i > 0:
                set_score[i - 1] *= 2

        elif m.group("option") == "#":
            local_score *= -1

        set_score[i] = local_score

    return sum(set_score)
