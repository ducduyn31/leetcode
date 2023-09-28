import unittest
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    count += 1

        return count


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.count_pairs = Solution().countPairs

    def test_1(self) -> None:
        self.assertEqual(self.count_pairs([-1, 1, 2, 3, 1], 2), 3)

    def test_2(self) -> None:
        self.assertEqual(self.count_pairs([-6, 2, 5, -2, -7, -1, 3], -2), 10)
