from typing import *


def solution() -> None:
    num_case: int = int(input().strip())

    for i in range(num_case):
        input_data: List[str] = input().strip().split()
        
        answer: str = ""
        for ch in input_data[1]:
            answer += ch * int(input_data[0])

        print(answer)
