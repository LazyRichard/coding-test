from typing import *
from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize("test_input,expected", [
    ["5 8 4", ["1", "1", "0", "0"]]
])
def test_solution(capsys, test_input: str, expected: List[str]) -> None:
    with mock.patch("builtins.input", lambda: test_input + "\n"):
        solution()
        captured = capsys.readouterr()

        assert captured.out == "\n".join(expected) + "\n"