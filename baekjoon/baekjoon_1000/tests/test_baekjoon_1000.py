from unittest import mock

import pytest

from .. import solution


@pytest.mark.parametrize("test_input,expected", [["2 3", "5\n"]])
def test_baekjoon_1000(capsys, test_input: str, expected: int) -> None:
    with mock.patch("builtins.input", lambda: test_input):
        solution()
        captured = capsys.readouterr()

        assert captured.out == expected
