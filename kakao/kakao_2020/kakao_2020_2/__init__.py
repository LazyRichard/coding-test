from __future__ import annotations
from typing import *


def solution(p: str) -> str:
    pb = Brackets(p)

    if pb.is_correct:
        return p

    answer: str = ""

    def _func(target: Brackets) -> str:
        ret: str = ""

        if str(target) == "":
            return ""

        u: Brackets
        v: Brackets
        u, v = target.split()

        if u.is_correct:
            return "{}{}".format(str(u), _func(v))

        ret += "({})".format(_func(v))

        tmp: str = str(u)[1 : len(str(u)) - 1]
        t: str
        tr: str = ""
        for i in range(len(tmp)):
            tr += "(" if tmp[i] == ")" else ")"

        return ret + tr

    return _func(pb)


class Brackets:
    def __init__(self, bracket_str: str, skip_check: bool = False) -> None:
        self._incorrect: bool = False
        self._balanced: bool = False
        self._target_str: str = bracket_str

        self._calc_str(bracket_str)

    def __len__(self) -> int:
        return len(self._target_str)

    def __str__(self) -> str:
        return self._target_str

    def __repr__(self) -> str:
        return "<{} '{}'>".format(self.__class__.__name__, self._target_str)

    @property
    def is_correct(self) -> bool:
        return not self._incorrect

    @property
    def is_balanced(self) -> bool:
        return self._balanced

    def split(self) -> Tuple[Brackets, Brackets]:
        target_lst: List[str] = list(self._target_str)
        prev_b: str = ""
        result_a: List[str] = []
        stk: List[str] = []

        while len(target_lst):
            curr: str = target_lst.pop(0)
            result_a.append(curr)

            if prev_b and prev_b != curr:
                stk.pop()
                if len(stk) == 0:
                    break
            else:
                prev_b = curr
                stk.append(curr)

        return (Brackets("".join(result_a)), Brackets("".join(target_lst)))

    def _calc_str(self, p: str) -> None:
        brk_stk = []
        cnt_brk: Dict[str, int] = {"open": 0, "close": 0}

        balanced: bool = False
        incorrect: bool = False

        for brk in p:
            if brk == "(":
                cnt_brk["open"] += 1
                brk_stk.append("(")
            elif brk == ")":
                cnt_brk["close"] += 1

                if not incorrect:
                    try:
                        brk_stk.pop()
                    except IndexError:
                        self._incorrect = True

        if cnt_brk["open"] == cnt_brk["close"]:
            self._balanced = True
