from typing import *
from unittest import mock
import io

import pytest

from .. import solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [
            ["5", "1 1", "12 34", "5 500", "40 60", "1000 1000"],
            ["2", "46", "505", "100", "2000"],
        ],
    ],
)
def test_solution(
    monkeypatch, capsys, test_input: List[str], expected: List[str]
) -> None:
    iter_input: Iterator = iter(test_input)

    with mock.patch("sys.stdin.readline", lambda: "{}".format(next(iter_input) + "\n")):
        solution()
        captured = capsys.readouterr()

        assert captured.out == "\n".join(expected) + "\n"
