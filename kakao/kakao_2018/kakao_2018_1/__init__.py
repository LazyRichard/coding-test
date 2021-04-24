from typing import List, Callable


def solution(n: int, map1: List[int], map2: List[int]) -> List[str]:
    decode_map_func = lambda x: list(bin(x).replace("0b", "").zfill(n))

    bin_map1 = list(map(decode_map_func, map1))
    bin_map2 = list(map(decode_map_func, map2))

    result: List[str] = []
    for i in range(len(bin_map1)):
        row: str = ""
        for j in range(len(bin_map1[0])):
            row = (row + "#") if bin_map1[i][j] == "1" or bin_map2[i][j] == "1" else (row + " ")

        result.append(row)

    return result

def solution2(n: int, map1: List[int], map2: List[int]) -> List[str]:
    result: List[str] = []

    for i, j in zip(map1, map2):
        row = bin(i | j).replace("0b", "").zfill(n)
        row = row.replace("1", "#")
        row = row.replace("0", " ")

        result.append(row)

    return result
