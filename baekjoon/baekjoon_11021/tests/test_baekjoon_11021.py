from typing import *
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [
            ["5", "1 1", "2 3", "3 4", "9 8", "5 2"],
            ["Case #1: 2", "Case #2: 5", "Case #3: 7", "Case #4: 17", "Case #5: 7"],
        ],
    ],
)
def test_solution(capsys, test_input: List[str], expected: List[str]) -> None:
    iter_input: Iterator = iter(test_input)

    with mock.patch("builtins.input", lambda: next(iter_input) + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == "\n".join(expected) + "\n"
