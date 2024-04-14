import unittest
import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, right - 1]


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.search_range = Solution().searchRange

    def test_1(self):
        self.assertEqual(self.search_range([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_2(self):
        self.assertEqual(self.search_range([5, 7, 7, 8, 8, 10], 6), [-1, -1])

    def test_3(self):
        self.assertEqual(self.search_range([], 0), [-1, -1])
