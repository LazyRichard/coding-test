from typing import Optional, Dict

def solution():
    test_input = int(input())

    prev_val: Dict[str, int] = {}
    new_val: Optional[int] = None
    cnt: int = 1

    while True:
        if not prev_val:
            prev_val["10"] = test_input // 10
            prev_val["1"] = test_input % 10
        else:
            prev_val["10"] = new_val // 10
            prev_val["1"] = new_val % 10

        calc_val:int = prev_val["10"] + prev_val["1"]
        new_val = int("{}{}".format(prev_val["1"], calc_val % 10))

        if new_val == test_input:
            break

        cnt = cnt + 1

    print(cnt)
