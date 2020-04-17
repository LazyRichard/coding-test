from typing import *
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize("test_input,expected", [
    [["100"], ["A"]],
    [["90"], ["A"]],
    [["65"], ["D"]],
    [["10"], ["F"]],
])
def test_solution(capsys, test_input: List[str], expected: List[str]) -> None:
    iter_input: Iterator = iter(test_input)

    with mock.patch("builtins.input", lambda: next(iter_input) + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == "\n".join(expected) + "\n"
