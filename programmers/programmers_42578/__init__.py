from typing import Dict, List, Tuple

def solution(clothes:Tuple[str, str]) -> int:
    clothes_by_type:Dict[str, int] = {}
    for cloth in clothes:
        try:
            clothes_by_type[cloth[1]]
        except KeyError:
            clothes_by_type[cloth[1]] = 1
        else:
            clothes_by_type[cloth[1]] = clothes_by_type[cloth[1]] + 1

    answer:int = 1
    for key, value in clothes_by_type.items():
        answer = answer * (value + 1)

    return answer - 1
