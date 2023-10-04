import unittest
from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(turn, start, end):
            alpha = turn % 2 * 2 - 1
            if start == end:
                return -alpha * nums[end]
            select = max if turn % 2 == 0 else min
            return select(
                dp(turn + 1, start, end - 1) - alpha * nums[end],
                dp(turn + 1, start + 1, end) - alpha * nums[start],
            )

        return dp(0, 0, len(nums) - 1) >= 0


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.predict_the_winner = Solution().predictTheWinner

    def test_1(self):
        self.assertEqual(self.predict_the_winner([1, 5, 2]), False)

    def test_2(self):
        self.assertEqual(self.predict_the_winner([1, 5, 233, 7]), True)
