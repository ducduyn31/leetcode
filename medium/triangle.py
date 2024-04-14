import unittest
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for line in range(len(triangle) - 2, -1, -1):
            for cell in range(line + 1):
                triangle[line][cell] += min(triangle[line + 1][cell], triangle[line + 1][cell + 1])

        return triangle[0][0]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.minimum_total = Solution().minimumTotal

    def test_minimum_total_should_return_11_given_4_lines(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

        self.assertEqual(11, self.minimum_total(triangle))

    def test_minimum_total_should_return_minus_10_given_1_line(self):
        triangle = [[-10]]

        self.assertEqual(-10, self.minimum_total(triangle))
