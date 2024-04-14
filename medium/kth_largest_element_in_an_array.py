import heapq
import unittest
from collections import Counter
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        counter = [0] * (max(nums) - min_val + 1)

        for i in nums:
            counter[i - min_val] += 1

        for i in range(len(counter) - 1, -1, -1):
            if counter[i] == 0:
                continue
            k -= counter[i]

            if k <= 0:
                return i + min_val

        return min_val


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.find_kth = Solution().findKthLargest

    def test_find_kth_should_return_5_given_k2(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(5, self.find_kth(nums, k))

    def test_find_kth_should_return_4_given_k4(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(4, self.find_kth(nums, k))

    def test_find_kth_should_return_minus1_given_k2(self):
        nums = [-1, -1]
        k = 2
        self.assertEqual(-1, self.find_kth(nums, k))
