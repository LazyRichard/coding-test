from typing import List, Iterator
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [["4 5 1", "1 2", "1 3", "1 4", "2 4", "3 4"], "1 2 4 3\n1 2 3 4"],
        [["5 5 3", "5 4", "5 2", "1 2", "3 4", "3 1"], "3 1 2 5 4\n3 1 4 2 5"],
        [["1000 1 1000", "999 1000"], "1000 999\n1000 999"],
    ],
)
def test_solution(capsys, test_input: List[str], expected: str) -> None:
    test_iter_input: Iterator = iter(test_input)

    with mock.patch("builtins.input", lambda: next(test_iter_input) + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == expected + "\n"
