import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_nums, lis = [], []

        for i, v in enumerate(nums):
            max_lis = bisect_left(sorted_nums, v)
            if max_lis == len(sorted_nums):
                sorted_nums.append(v)
                lis.append([i])
            else:
                sorted_nums[max_lis] = v
                lis[max_lis].append(i)

        return len(lis)


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.length_of_lis = Solution().lengthOfLIS

    def test_length_of_lis_should_return_4_given_8_elements(self):
        self.assertEqual(4, self.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))

    def test_length_of_lis_should_return_4_given_6_elements(self):
        self.assertEqual(4, self.length_of_lis([0, 1, 0, 3, 2, 3]))

    def test_length_of_lis_should_return_1_given_7_elements(self):
        self.assertEqual(1, self.length_of_lis([7, 7, 7, 7, 7, 7, 7]))

    def test_length_of_lis_should_return_6_given_9_elements(self):
        self.assertEqual(6, self.length_of_lis([1, 3, 6, 7, 9, 4, 10, 5, 6]))
