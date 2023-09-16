import unittest
from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        max_id = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[max_id]:
                max_id = i
            else:
                break

        for j in range(max_id + 2, len(nums)):
            if nums[j] < nums[j - 1] or nums[j] > nums[max_id]:
                return -1

        return len(nums) - max_id - 1


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.min_right_shifts = Solution().minimumRightShifts

    def test_1(self):
        self.assertEqual(2, self.min_right_shifts([3, 4, 5, 1, 2]))

    def test_2(self):
        self.assertEqual(0, self.min_right_shifts([1, 3, 5]))

    def test_3(self):
        self.assertEqual(-1, self.min_right_shifts([2, 1, 4]))
