import unittest
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
        result = []
        index_max = deque()

        for i in range(len(nums)):
            while index_max and nums[index_max[-1]] < nums[i]:
                index_max.pop()
            index_max.append(i)
            if i >= k - 1:
                result.append(nums[index_max[0]])

            while index_max and i - k + 1 >= index_max[0]:
                index_max.popleft()

        return result


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.max_sliding_window = Solution().maxSlidingWindow

    def test_max_sliding_window_should_for_k3_and_len_8(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual([3, 3, 5, 5, 6, 7], self.max_sliding_window(nums, k))

    def test_max_sliding_window_should_for_k1_and_len_1(self):
        nums = [1]
        k = 1
        self.assertEqual([1], self.max_sliding_window(nums, k))

    def test_max_sliding_window_should_for_k1_and_len_2(self):
        nums = [1, -1]
        k = 1
        self.assertEqual([1, -1], self.max_sliding_window(nums, k))

    def test_max_sliding_window_should_for_k3_and_len_6(self):
        nums = [1, 3, 1, 2, 0, 5]
        k = 3
        self.assertEqual([3, 3, 2, 5], self.max_sliding_window(nums, k))
