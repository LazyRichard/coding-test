from typing import List


def solution(test_input: str) -> int:
    if len(test_input) == 1:
        return 1
    
    answer: List[int] = []
    for i in range(1, (len(test_input) // 2) + 1):
        temp: List[str] = []
        for j in range(0, len(test_input), i):
            temp.append(test_input[j:(j + i)])

        answer.append(len(compress(temp)))

    return min(answer)

def compress(word_list: List[str]) -> str:
    answer: str = ""
    test_ch: str = ""
    cnt:int = 1

    for ch in word_list:
        if not test_ch:
            test_ch = ch
        else:
            if test_ch == ch:
                cnt = cnt + 1
            elif test_ch != ch and cnt == 1:
                answer = answer + test_ch
                test_ch = ch
            else:
                answer = answer + "{}{}".format(cnt, test_ch)
                test_ch = ch
                cnt = 1

    if cnt > 1:
        answer = answer + "{}{}".format(cnt, test_ch)
    else:
        answer = answer + test_ch

    return answer