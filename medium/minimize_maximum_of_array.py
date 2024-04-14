import math
import unittest
from functools import cache
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        last_sum = nums[-1]
        count = 1

        max_value = last_sum

        for i in range(n - 2, -1, -1):
            if last_sum // count < nums[i]:
                max_value = min(max_value, math.ceil(last_sum / count))
                last_sum = nums[i]
                count = 1
            else:
                last_sum += nums[i]
                count += 1

        return max_value


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.minimize_array_value = Solution().minimizeArrayValue

    def test_1(self):
        nums = [3, 7, 1, 6]
        self.assertEqual(5, self.minimize_array_value(nums))

    def test_2(self):
        nums = [10, 1]
        self.assertEqual(10, self.minimize_array_value(nums))

    def test_3(self):
        nums = [13, 13, 20, 0, 8, 9, 9]
        self.assertEqual(16, self.minimize_array_value(nums))

    def test_4(self):
        nums = [4, 7, 2, 2, 9, 19, 16, 0, 3, 15]
        self.assertEqual(9, self.minimize_array_value(nums))
