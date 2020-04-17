from typing import *
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize("test_input,expected", [
    [["2", "3 ABC", "5 /HTP"], ["AAABBBCCC", "/////HHHHHTTTTTPPPPP"]],
])
def test_solution(capsys, test_input: List[str], expected: List[str]) -> None:
    iter_input: Iterator = iter(test_input)

    with mock.patch("builtins.input", lambda: next(iter_input) + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == "\n".join(expected) + "\n"
