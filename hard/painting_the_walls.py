import unittest
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.paint_walls = Solution().paintWalls

    def test_1(self):
        cost = [1, 2, 3, 2]
        time = [1, 2, 3, 2]

        self.assertEqual(3, self.paint_walls(cost, time))

    def test_2(self):
        cost = [2, 3, 4, 2]
        time = [1, 1, 1, 1]

        self.assertEqual(4, self.paint_walls(cost, time))
