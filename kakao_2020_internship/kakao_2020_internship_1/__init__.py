from typing import *


def solution(numbers: List[int], hand: str) -> str:
    thumb_pos: Dict[str, Tuple[int, int]] = {"left": (0, 0), "right": (2, 0)}

    answer: List[str] = []

    for num in numbers:
        target_pos: Optional[Tuple[int, int]] = None

        # Left thumb
        if num == 1:
            thumb_pos["left"] = (0, 3)
            answer.append("L")
            continue
        elif num == 4:
            thumb_pos["left"] = (0, 2)
            answer.append("L")
            continue
        elif num == 7:
            thumb_pos["left"] = (0, 1)
            answer.append("L")
            continue
        # Right thumb
        elif num == 3:
            thumb_pos["right"] = (2, 3)
            answer.append("R")
            continue
        elif num == 6:
            thumb_pos["right"] = (2, 2)
            answer.append("R")
            continue
        elif num == 9:
            thumb_pos["right"] = (2, 1)
            answer.append("R")
            continue
        elif num == 2:
            target_pos = (1, 3)
        elif num == 5:
            target_pos = (1, 2)
        elif num == 8:
            target_pos = (1, 1)
        elif num == 0:
            target_pos = (1, 0)

        if target_pos:
            dist_l = calc_dist(thumb_pos["left"], target_pos)
            dist_r = calc_dist(thumb_pos["right"], target_pos)

            if dist_l > dist_r:
                thumb_pos["right"] = target_pos
                answer.append("R")
            elif dist_l < dist_r:
                thumb_pos["left"] = target_pos
                answer.append("L")
            else:
                if hand == "left":
                    thumb_pos["left"] = target_pos
                    answer.append("L")
                else:
                    thumb_pos["right"] = target_pos
                    answer.append("R")

    return "".join(answer)


def calc_dist(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])
