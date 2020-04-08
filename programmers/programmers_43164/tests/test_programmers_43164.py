from typing import List

import pytest

from .. import solution


@pytest.mark.parametrize(
    "tickets,expected",
    [
        [
            [
                ["ICN", "JFK"],
                ["HND", "IAD"],
                ["JFK", "HND"]
            ],
            ["ICN", "JFK", "HND", "IAD"],
        ],
        [
            [
                ["ICN", "SFO"],
                ["ICN", "ATL"],
                ["SFO", "ATL"],
                ["ATL", "ICN"],
                ["ATL", "SFO"],
            ],
            ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
        ],
        [
            [
                ["ICN", "COO"],
                ["ICN", "BOO"],
                ["COO", "ICN"],
                ["BOO", "DOO"]
            ],
            ["ICN", "COO", "ICN", "BOO", "DOO"],
        ],
        [
            [
                ["ICN", "BOO"],
                ["ICN", "COO"],
                ["COO", "DOO"],
                ["DOO", "COO"],
                ["BOO", "DOO"],
                ["DOO", "BOO"],
                ["BOO", "ICN"],
                ["COO", "BOO"],
            ],
            ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO'],
        ],
    ],
)
def test_solution(tickets: List[List[str]], expected: List[str]) -> None:
    assert solution(tickets) == expected
