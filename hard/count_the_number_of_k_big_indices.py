import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        left_indices, right_indices = set(), set()

        values = []
        for i, n in enumerate(nums):
            order = bisect_left(values, n)

            if order == len(values):
                values.append(n)
            else:
                values[order] = n

            if order >= k:
                left_indices.add(i)

        values = []
        for i in range(len(nums) - 1, -1, -1):
            order = bisect_left(values, nums[i])

            if order == len(values):
                values.append(nums[i])
            else:
                values[order] = nums[i]

            if order >= k:
                right_indices.add(i)

        return len(left_indices.intersection(right_indices))


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.k_big_indices = Solution().kBigIndices

    def test_k_big_indices_should_return_2_given_k_2(self):
        self.assertEqual(2, self.k_big_indices([2, 3, 6, 5, 2, 3], 2))

    def test_k_big_indices_should_return_0_given_k_3(self):
        self.assertEqual(0, self.k_big_indices([1, 1, 1], 3))
