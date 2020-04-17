from typing import *
import difflib

"""
graph: {
    "hit": [("log", 1), ("log": 1)],
    "log": [("hit", 1)]
}
"""

class Edge(NamedTuple):
    dest_vert: str
    weight: int

def solution(begin: str, target: str, words: List[str]) -> int:
    output: List[List[str]] = []
    graph: Dict[str, List[Edge]] = {
        "begin": []
    }

    graph = create_graph(begin, words)

    return 0

def create_graph(begin, words):
    graph = {}
    used: List[str] = [begin]

    def _create_graph(nxt: str):
        for word in words:
            if diff_letters(nxt, word) == 1 and word not in used:
                used.append(word)
                add_edge(graph, nxt, word)

        _create_graph(word)

    _create_graph(begin)

    return graph

def add_vertex(graph: Dict[str, List[Edge]], vertex: str):
    graph[vertex] = []

def add_edge(graph: Dict[str, List[Edge]], from_vert: str, dest_vert: str, weight: int = 1):
    if from_vert not in graph.keys():
        add_vertex(graph, from_vert)
    
    if dest_vert not in graph.keys():
        add_vertex(graph, dest_vert)

    graph[from_vert].append(Edge(dest_vert=dest_vert, weight=weight))
    graph[dest_vert].append(Edge(dest_vert=from_vert, weight=weight))



def diff_letters(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))