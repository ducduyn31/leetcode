import unittest
from functools import cache
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        @cache
        def dp(n):
            if n == 0:
                return 1

            candidates = []

            for i in range(n):
                if nums[i] <= nums[n]:
                    candidates.append(1 + dp(i))
                else:
                    candidates.append(1)
            return max(candidates)

        lis_len = max(dp(i) for i in range(len(nums)))

        return len(nums) - lis_len


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.minimum_operations = Solution().minimumOperations

    def test_1(self) -> None:
        self.assertEqual(self.minimum_operations([2, 1, 3, 2, 1]), 3)

    def test_2(self) -> None:
        self.assertEqual(self.minimum_operations([1, 3, 2, 1, 3, 3]), 2)

    def test_3(self) -> None:
        self.assertEqual(self.minimum_operations([2, 2, 2, 2, 3, 3]), 0)

    def test_4(self) -> None:
        self.assertEqual(self.minimum_operations([3, 3, 2]), 1)
