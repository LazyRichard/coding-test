from typing import *
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize("test_input,expected", [[["5", "6 9 5 7 4"], "0 0 2 2 4"]])
def test_solution(capsys, test_input: str, expected: str) -> None:
    test_input_iter: Iterator = iter(test_input)

    with mock.patch("builtins.input", lambda: next(test_input_iter) + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == expected + "\n"
