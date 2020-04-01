from typing import List
import re

def solution(phone_book:List[str]) -> bool:
    min_ele:str = min(phone_book, key=len)

    pattern:str = "^{}".format(min_ele)

    find_cnt = 0
    for phone_number in phone_book:
        if re.search(pattern, phone_number) is not None:
            find_cnt = find_cnt + 1
            if find_cnt > 1:
                return False

    return True
