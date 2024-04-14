import unittest
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            for j in range(n - i):
                if i == 0:
                    dp[j] = nums[j]
                else:
                    dp[j] = max(
                        nums[i + j] - dp[j],
                        nums[j] - dp[j + 1],
                    )

        return dp[0] >= 0


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.predict_the_winner = Solution().predictTheWinner

    def test_1(self):
        self.assertEqual(self.predict_the_winner([1, 5, 2]), False)

    def test_2(self):
        self.assertEqual(self.predict_the_winner([1, 5, 233, 7]), True)

    def test_3(self):
        self.assertEqual(self.predict_the_winner([2, 4, 55, 6, 8]), False)
