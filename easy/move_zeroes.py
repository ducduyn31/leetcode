import unittest
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0
        n = len(nums)

        while right < n:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

            right += 1

        while left < n:
            nums[left] = 0
            left += 1


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.move_zeroes = Solution().moveZeroes

    def test_1(self):
        nums = [ 0 , 1, 0, 3, 12]
        #              1,  3, ^       ^
        self.move_zeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_2(self):
        nums = [0]
        self.move_zeroes(nums)
        self.assertEqual(nums, [0])
