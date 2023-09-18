import bisect
import unittest
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        mid = N // 2
        count = bisect.bisect_right(nums, nums[mid]) - bisect.bisect_left(nums, nums[mid])
        if count > mid:
            return 2 * count - N
        return N % 2


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.min_length_after_removals = Solution().minLengthAfterRemovals

    def test_1(self):
        self.assertEqual(0, self.min_length_after_removals([1, 3, 4, 9]))

    def test_2(self):
        self.assertEqual(0, self.min_length_after_removals([2, 3, 6, 9]))

    def test_3(self):
        self.assertEqual(1, self.min_length_after_removals([1, 1, 2]))

    def test_4(self):
        self.assertEqual(1, self.min_length_after_removals([1, 3, 3, 3, 4]))

    def test_5(self):
        self.assertEqual(1, self.min_length_after_removals([1]))

    def test_6(self):
        self.assertEqual(1, self.min_length_after_removals([2, 3, 4]))

    def test_7(self):
        self.assertEqual(0, self.min_length_after_removals([1, 1, 2, 3, 4, 4]))

    def test_8(self):
        self.assertEqual(0, self.min_length_after_removals([1, 1, 2, 2, 4, 4]))

    def test_9(self):
        self.assertEqual(3, self.min_length_after_removals([1, 1, 1, 1, 1, 4, 4]))
