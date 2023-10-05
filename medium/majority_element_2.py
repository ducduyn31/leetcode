import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x1, x2, c1, c2 = 0, 0, 0, 0
        l = len(nums) // 3

        for x in nums:
            if c1 == 0 and x != x2:
                x1 = x
                c1 += 1
            elif c2 == 0 and x != x1:
                x2 = x
                c2 += 1
            elif x == x1:
                c1 += 1
            elif x == x2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        c1, c2 = 0, 0

        for x in nums:
            if x == x1:
                c1 += 1
            elif x == x2:
                c2 += 1

        ans = []

        if c1 > l:
            ans.append(x1)
        if c2 > l:
            ans.append(x2)

        return ans


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.majority_element = Solution().majorityElement

    def test_1(self):
        nums = [3, 2, 3]
        self.assertEqual([3], self.majority_element(nums))

    def test_2(self):
        nums = [1, 1, 1, 3, 3, 2, 2, 2]
        self.assertEqual([1, 2], self.majority_element(nums))

    def test_3(self):
        nums = [1]
        self.assertEqual([1], self.majority_element(nums))
