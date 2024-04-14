import unittest
from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        valid = [False] * len(nums)

        def update_valid(start: int):
            if start < len(valid) - 1 and nums[start] == nums[start + 1]:
                valid[start + 1] = True

            if start < len(valid) - 2:
                valid[start + 2] = nums[start] == nums[start + 1] == nums[start + 2] or nums[start] + 2 == nums[
                    start + 1] + 1 == nums[start + 2]

        update_valid(0)
        i = 1
        while i < len(valid):
            if valid[i - 1]:
                update_valid(i)
            i += 1

        return valid[-1]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_partition = Solution().validPartition

    def test_valid_partition_should_return_true_given_4_4_4_5_6(self):
        nums = [4, 4, 4, 5, 6]
        self.assertTrue(self.valid_partition(nums))

    def test_valid_partition_should_return_false_given_1_1_1_2(self):
        nums = [1, 1, 1, 2]
        self.assertFalse(self.valid_partition(nums))
