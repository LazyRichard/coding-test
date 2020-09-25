from typing import *


def solution() -> None:
    num_word: int = int(input().strip())
    answer: int = 0

    for i in range(num_word):
        word: str = input().strip()

        is_group_word: bool = True
        last_ch: str = next(iter(word))
        cnt: Dict[str, int] = {last_ch: 1}
        ch: str
        for ch in word:
            if last_ch != ch:

                if ch in cnt.keys():
                    is_group_word = False
                    break

            cnt[ch] = 1

            last_ch = ch

        if is_group_word:
            answer += 1

    print(answer)
