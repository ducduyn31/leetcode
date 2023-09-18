import unittest
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        left, right = 0, len(nums) // 2

        def can_remove_completely(k: int):
            for i in range(k):
                if nums[i] >= nums[-k + i]:
                    return False
            return True

        while left < right:
            mid = (left + right + 1) // 2

            if can_remove_completely(mid):
                left = mid
            else:
                right = mid - 1

        return len(nums) - 2 * left


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
