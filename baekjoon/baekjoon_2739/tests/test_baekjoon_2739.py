from typing import *
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [
            ["2"],
            [
                "2 * 1 = 2",
                "2 * 2 = 4",
                "2 * 3 = 6",
                "2 * 4 = 8",
                "2 * 5 = 10",
                "2 * 6 = 12",
                "2 * 7 = 14",
                "2 * 8 = 16",
                "2 * 9 = 18",
            ],
        ]
    ],
)
def test_solution(capsys, test_input: List[str], expected: List[str]) -> None:
    iter_input: Iterator = iter(test_input)

    with mock.patch("builtins.input", lambda: next(iter_input) + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == "\n".join(expected) + "\n"
