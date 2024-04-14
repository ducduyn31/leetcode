import unittest
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.maximal_rectangle = Solution().maximalRectangle

    def test_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        self.assertEqual(6, self.maximal_rectangle(matrix))

    def test_2(self):
        matrix = [["1"]]
        self.assertEqual(1, self.maximal_rectangle(matrix))

    def test_3(self):
        matrix = [["0"]]
        self.assertEqual(0, self.maximal_rectangle(matrix))