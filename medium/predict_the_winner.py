import unittest
from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(turn, start, end):
            if start == end:
                return nums[end]
            return max(
                nums[end] - dp(turn + 1, start, end - 1),
                nums[start] - dp(turn + 1, start + 1, end)
            )

        return dp(0, 0, len(nums) - 1) >= 0


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.predict_the_winner = Solution().predictTheWinner

    def test_1(self):
        self.assertEqual(self.predict_the_winner([1, 5, 2]), False)

    def test_2(self):
        self.assertEqual(self.predict_the_winner([1, 5, 233, 7]), True)
