import pytest

from programmers_42576 import solution

@pytest.mark.parametrize(
    "participant,completion,expected",
    [
        [["leo", "kiki", "eden"], ["eden", "kiki"],"leo"],
        [["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"], "vinko"],
        [["a"], [], "a"]
    ])
def test_solution_no_dups(participant, completion, expected):
    assert expected == solution(participant, completion)

@pytest.mark.parametrize(
    "participant,completion,expected",
    [
        [["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"], "mislav"],
        [["a", "a", "a", "b"], ["a", "a", "a"], "b"],
        [["a", "b", "c", "d", "d"], ["a", "b", "c", "d"], "d"],
        [["a", "a", "b", "b", "c", "c", "d"], ["a", "a", "c", "c", "d", "b"], "b"]
    ]
)
def test_solution_dups(participant, completion, expected):
    assert expected == solution(participant, completion)