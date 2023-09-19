import unittest
from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def filter_diagonal_positions(available: set, queens: list, current_row: int):
            filtered = set()

            for current_col in available:
                if any(current_row - row == abs(current_col - col) for row, col in enumerate(queens)):
                    continue
                filtered.add(current_col)

            return filtered

        def helper(level: int, current_variation: list, available: set):
            if level == 0:
                temp = []
                for col in current_variation:
                    templ = ['.'] * n
                    templ[col] = 'Q'
                    temp.append(''.join(templ))
                result.append(temp[:])
                return

            filtered_pos = filter_diagonal_positions(available, current_variation, n - level)

            for i in filtered_pos:
                current_variation.append(i)
                available.remove(i)
                helper(level - 1, current_variation, available)
                available.add(i)
                current_variation.pop()

        helper(n, [], set(range(n)))

        return result


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.solve_n_queens = Solution().solveNQueens

    def test_1(self) -> None:
        self.assertEqual(self.solve_n_queens(4), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])

    def test_2(self) -> None:
        self.assertEqual(self.solve_n_queens(1), [["Q"]])
