import unittest
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.max_sum = Solution().maxSum

    def test_1(self):
        self.assertEqual(261, self.max_sum([2, 6, 5, 8], k=2))

    def test_2(self):
        self.assertEqual(90, self.max_sum([4, 5, 4, 7], k=3))
