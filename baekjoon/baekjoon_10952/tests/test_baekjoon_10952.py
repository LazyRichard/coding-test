from typing import Iterable, Tuple
from unittest import mock

import pytest

from .. import solution


def test_solution(capsys) -> None:
    test_input = iter(["1 1\n", "2 3\n", "3 4\n", "9 8\n", "5 2\n", "0 0\n"])
    expected = "2\n5\n7\n17\n7\n"

    with mock.patch("builtins.input", lambda: next(test_input)):
        solution()
        captured = capsys.readouterr()

        assert captured.out == expected
