import unittest
from itertools import groupby
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()

        prev_num = 0
        first, second = 0, 0

        for x, group in groupby(nums):
            if x == prev_num + 1:
                first, second = second, max(first + x * len(list(group)), second)
            else:
                first, second = second, second + x * len(list(group))
            prev_num = x

        return second


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.delete_and_earn = Solution().deleteAndEarn

    def test_1(self):
        nums = [3, 4, 2]
        self.assertEqual(6, self.delete_and_earn(nums))

    def test_2(self):
        nums = [2, 2, 3, 3, 3, 4]
        self.assertEqual(9, self.delete_and_earn(nums))
