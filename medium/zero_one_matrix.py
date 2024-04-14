import unittest
from math import inf
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = [row[:] for row in mat]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    continue

                min_neighbor = inf
                if row > 0:
                    min_neighbor = min(min_neighbor, result[row - 1][col])
                if col > 0:
                    min_neighbor = min(min_neighbor, result[row][col - 1])

                result[row][col] = min_neighbor + 1

        for row in range(len(mat) - 1, -1, -1):
            for col in range(len(mat[0]) - 1, -1, -1):
                if mat[row][col] == 0:
                    continue

                min_neighbor = inf
                if row < len(mat) - 1:
                    min_neighbor = min(min_neighbor, result[row + 1][col])
                if col < len(mat[0]) - 1:
                    min_neighbor = min(min_neighbor, result[row][col + 1])

                result[row][col] = min(min_neighbor + 1, result[row][col])

        return result


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.update_matrix = Solution().updateMatrix

    def test_update_matrix_case_1(self):
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(expected, self.update_matrix(mat))

    def test_update_matrix_case_2(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        self.assertEqual(expected, self.update_matrix(mat))

    def test_update_matrix_case_3(self):
        mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
               [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
        expected = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 2, 1, 1, 0, 1], [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
                    [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]
        self.assertEqual(expected, self.update_matrix(mat))
