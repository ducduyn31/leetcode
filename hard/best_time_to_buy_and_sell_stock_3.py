import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_profits, max_right = [0], 0
        left_profits, max_left = [0], 0

        for i in range(len(prices) - 2, -1, -1):
            max_right = max(max_right + prices[i + 1] - prices[i], prices[i + 1] - prices[i])
            right_profits.append(max(max_right, right_profits[-1]))

        for i in range(0, len(prices) - 1):
            max_left = max(max_left + prices[i + 1] - prices[i], prices[i + 1] - prices[i])
            left_profits.append(max(max_left, left_profits[-1]))

        return max(a + b for a, b in zip(left_profits, reversed(right_profits)))


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.max_profit = Solution().maxProfit

    def test_max_profit_should_return_6_within_8_days(self):
        self.assertEqual(6, self.max_profit([3, 3, 5, 0, 0, 3, 1, 4]))

    def test_max_profit_should_return_4_within_5_days(self):
        self.assertEqual(4, self.max_profit([1, 2, 3, 4, 5]))

    def test_max_profit_should_return_0_within_5_days(self):
        self.assertEqual(0, self.max_profit([7, 6, 4, 3, 1]))

    def test_max_profit_should_return_3_within_3_days(self):
        self.assertEqual(3, self.max_profit([2, 1, 4]))

    def test_max_profit_should_return_13_within_10_days(self):
        self.assertEqual(13, self.max_profit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
