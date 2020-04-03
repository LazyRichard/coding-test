from typing import Tuple, List
from collections import deque


def solution():
    num_vert: int
    num_edge: int
    start_vert: int
    num_vert, num_edge, start_vert = map(int, input().strip().split())

    graph: List[List[int]] = [[0 for _ in range(num_vert)] for __ in range(num_vert)]

    for i in range(num_edge):
        edge: Tuple[int, int] = tuple(
            map(lambda x: int(x) - 1, input().strip().split())
        )

        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1

    print(" ".join(map(lambda x: str(x + 1), dfs(graph, start_vert - 1))))
    print(" ".join(map(lambda x: str(x + 1), bfs(graph, start_vert - 1))))


def dfs(matrix: List[List[int]], start_vert: int) -> List[int]:
    stk: List[int] = [start_vert]
    visited: List[int] = [start_vert]

    def _vert():
        vert: int = stk.pop()

        for idx, x in enumerate(matrix[vert]):
            if x and idx not in visited:
                stk.append(idx)
                visited.append(idx)

                _vert()

    _vert()

    return visited


def bfs(matrix: List[List[int]], start_vert: int) -> List[int]:
    que: deque = deque([start_vert])
    visited: List[int] = [start_vert]

    while que:
        vert = que.popleft()

        for idx, x in enumerate(matrix[vert]):
            if x and idx not in visited:
                que.append(idx)
                visited.append(idx)

    return visited
