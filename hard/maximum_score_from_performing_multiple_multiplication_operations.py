import unittest
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.maximum_score = Solution().maximumScore

    def test_1(self):
        nums = [1, 2, 3]
        multipliers = [3, 2, 1]
        self.assertEqual(14, self.maximum_score(nums, multipliers))

    def test_2(self):
        nums = [-5, -3, -3, -2, 7, 1]
        multipliers = [-10, -5, 3, 4, 6]
        self.assertEqual(102, self.maximum_score(nums, multipliers))
