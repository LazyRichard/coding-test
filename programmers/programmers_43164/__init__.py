from typing import *

from collections import defaultdict

def solution(tickets: List[List[str]]) -> List[str]:
    graph: Dict[str, List[str]] = defaultdict(list)
    tickets_avaliable: Counter = Counter()
    path: List[str] = []

    ticket: List[str]
    for ticket in tickets:
        add_edge(graph, ticket[0], ticket[1], direction=True)

    key: str
    value: List[str]
    for key, value in graph.items():
        graph[key] = sorted(value)
        tickets_avaliable += Counter(graph[key])

    def _travel(dest: str, parent: Optional[str] = None) -> bool:
        if not parent:
            path.append(dest)

        for dst in graph[dest]:
            path.append(dst)
            graph[dest].remove(dst)

            if not _travel(dst, dest):
                path.pop()
                graph[dest].insert(0, dst)

        if sum(list(map(lambda x: len(x), graph.values()))) == 0:
            return True

        return False

    _travel("ICN")

    return path


def add_edge(
    graph: Dict[str, List[str]],
    from_vert: str,
    dest_vert: str,
    weight: int = 1,
    direction: bool = False,
) -> None:
    graph[from_vert].append(dest_vert)

    if not direction:
        graph[dest_vert].append(from_vert)
