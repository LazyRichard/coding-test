from typing import Iterable, Tuple
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize("test_input,expected", [
    ["26", "4"],
    ["55", "3"],
    ["1", "60"]
])
def test_solution(capsys, test_input: str, expected: str) -> None:
    with mock.patch("builtins.input", lambda: test_input + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == expected + "\n"
