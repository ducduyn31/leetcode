import unittest


class Solution:
    result = 0

    def totalNQueens(self, n: int) -> int:
        self.place_queen(n, 0, set())
        return self.result

    def place_queen(self, n: int, col: int, queens: set):
        if col == n and len(queens) == n:
            self.result += 1
            return

        taken = set()

        for queen_col, queen_row in queens:
            taken.add(queen_row)

            if queen_row - (col - queen_col) >= 0:
                taken.add(queen_row - (col - queen_col))

            if queen_row + (col - queen_col) < n:
                taken.add(queen_row + (col - queen_col))

        for row in range(n):
            if row in taken:
                continue
            queens.add((col, row))
            self.place_queen(n, col + 1, queens)
            queens.remove((col, row))


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.total_n_queens = Solution().totalNQueens

    def test_total_n_queens_should_return_1_given_1(self):
        self.assertEqual(1, self.total_n_queens(1))

    def test_total_n_queens_should_return_0_given_2(self):
        self.assertEqual(0, self.total_n_queens(2))

    def test_total_n_queens_should_return_2_given_4(self):
        self.assertEqual(2, self.total_n_queens(4))
