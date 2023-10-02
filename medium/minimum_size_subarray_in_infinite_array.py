import unittest
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        nums.extend(nums)
        min_len = (target // total_sum) * n
        target = target - total_sum * min_len // n

        start = end = 0
        current = nums[0]
        ans = float('inf')

        while start < n and end < 2 * n:
            if current < target:
                end += 1
                current += nums[end]
            elif current > target:
                current -= nums[start]
                start += 1
            else:
                ans = min(ans, min_len + end - start + 1)
                end += 1
                current += nums[end]

        if ans == float('inf') and min_len > 0 and target == 0:
            return min_len
        elif ans == float('inf'):
            return -1
        else:
            return ans


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.min_size_subarray = Solution().minSizeSubarray

    def test_1(self):
        self.assertEqual(self.min_size_subarray([1, 2, 3], 5), 2)

    def test_2(self):
        self.assertEqual(self.min_size_subarray([1, 1, 1, 2, 3], 4), 2)

    def test_3(self):
        self.assertEqual(self.min_size_subarray([2, 4, 6, 8], 3), -1)
