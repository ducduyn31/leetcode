import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0
        n = len(nums)

        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.remove_element = Solution().removeElement

    def test_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        self.assertEqual(self.remove_element(nums, val), 2)
        self.assertCountEqual(nums[:2], [2, 2])

    def test_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        self.assertEqual(self.remove_element(nums, val), 5)
        self.assertCountEqual(nums[:5], [0, 1, 3, 0, 4])
