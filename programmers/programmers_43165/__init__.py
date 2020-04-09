from typing import *

from collections import defaultdict, deque


class GenID:
    def __init__(self, start: int = 0):
        self._id: int = start

    def __iter__(self):
        return self

    def __next__(self):
        curr_id = self._id
        self._id += 1
        return curr_id


class Edge(NamedTuple):
    dest_vert: str
    weight: int


def solution(numbers: List[int], target: int) -> int:
    _id = GenID(start=1)
    graph: Dict[str, List[Edge]] = defaultdict(list)
    grp_que: deque = deque()

    graph["0"] = []
    grp_que.append("0")

    for num in numbers:
        for parent in list(grp_que):
            grp_que.popleft()

            child1 = str(next(_id))
            child2 = str(next(_id))
            grp_que.append(child1)
            grp_que.append(child2)

            add_edge(graph, parent, child1, num)
            add_edge(graph, parent, child2, -1 * num)

    answer: int = 0
    def _travel(dest: str, parent: Optional[str] = None, sum_weights: int = 0) -> None:
        nonlocal answer

        for dst in graph[dest]:
            if dst.dest_vert == parent:
                continue

            sum_temp: int = sum_weights + dst.weight

            # Check leaf
            if len(graph[dst.dest_vert]) == 1 and sum_temp == target:
                answer += 1

            _travel(dst.dest_vert, dest, sum_temp)

    _travel("0")

    return answer


def add_edge(
    graph: Dict[str, List[Edge]], from_vert: str, dest_vert: str, weight: int
) -> None:
    graph[from_vert].append(Edge(dest_vert=dest_vert, weight=weight))
    graph[dest_vert].append(Edge(dest_vert=from_vert, weight=weight))
