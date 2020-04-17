from typing import *
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize("test_input,expected", [
    ["7 3", "10\n4\n21\n2\n1"]
])
def test_solution(capsys, test_input: str, expected: str) -> None:
    with mock.patch("builtins.input", lambda: test_input + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == expected + "\n"
