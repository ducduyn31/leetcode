import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.max_area = Solution().maxArea

    def test_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.max_area(height), 49)

    def test_2(self):
        height = [1, 1]
        self.assertEqual(self.max_area(height), 1)
