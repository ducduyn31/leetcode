import unittest
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.exist_helper(board, word, row, col):
                        return True
        return False

    def exist_helper(self, board: List[List[str]], word: str, row: int, col: int) -> bool:
        if not word:
            return True

        temp = board[row][col]
        if temp == word[0]:
            board[row][col] = ''
        else:
            return False

        if col > 0 and self.exist_helper(board, word[1:], row, col - 1):
            return True

        if col < len(board[0]) - 1 and self.exist_helper(board, word[1:], row, col + 1):
            return True

        if row > 0 and self.exist_helper(board, word[1:], row - 1, col):
            return True

        if row < len(board) - 1 and self.exist_helper(board, word[1:], row + 1, col):
            return True

        if len(board) == len(board[0]) == 1 and not word[1:]:
            return True

        board[row][col] = temp

        return False


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.exist = Solution().exist

    def test_exist_should_true_given_A(self):
        board = [["A"]]
        self.assertTrue(self.exist(board, 'A'))

    def test_exist_should_true_given_ABCCED(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        self.assertTrue(self.exist(board, 'ABCCED'))

    def test_exist_should_true_given_SEE(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        self.assertTrue(self.exist(board, 'SEE'))

    def test_exist_should_false_given_ABCB(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        self.assertFalse(self.exist(board, 'ABCB'))
