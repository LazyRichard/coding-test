from typing import List, Optional


def solution(board: List[List[int]], moves: List[int]) -> int:
    bd = GameBoard(board)

    answer: int = 0

    buk: List[int] = []
    top: Optional[int] = None
    for mv in moves:
        crane: Optional[int] = bd.pop_item(mv - 1)

        if crane is not None and crane == top:
            buk.pop()
            try:
                top = buk[-1]
            except IndexError:
                top = None

            answer += 2
        elif crane is not None:
            top = crane
            buk.append(crane)

    return answer


class GameBoard:
    def __init__(self, list_board: List[List[int]]):
        self._board = self.load_item(list_board)

    def load_item(self, list_board: List[List[int]]) -> List[List[int]]:
        board: List[List[int]] = []

        for x in range(len(list_board[0])):
            # for y in range(len(list_board)):
            #    stk.append(list_board[y][x])
            stk: List[int] = [
                list_board[y][x]
                for y in range(len(list_board))
                if list_board[y][x] != 0
            ]

            board.append(stk)

        return board

    def pop_item(self, index: int) -> Optional[int]:
        item: Optional[int] = None

        try:
            item = self._board[index].pop(0)
        finally:
            return item
