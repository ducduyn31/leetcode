import unittest
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0

        for c in cost:
            first, second = second, min(first + c, second + c)

        return min(first, second)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.min_cost_climbing_stairs = Solution().minCostClimbingStairs

    def test_1(self):
        cost = [10, 15, 20]
        self.assertEqual(15, self.min_cost_climbing_stairs(cost))

    def test_2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(6, self.min_cost_climbing_stairs(cost))
