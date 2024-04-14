import unittest
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.max_dot_product = Solution().maxDotProduct

    def test_1(self):
        nums1 = [2, 1, -2, 5]
        nums2 = [3, 0, -6]
        self.assertEqual(18, self.max_dot_product(nums1, nums2))

    def test_2(self):
        nums1 = [3, -2]
        nums2 = [2, -6, 7]
        self.assertEqual(21, self.max_dot_product(nums1, nums2))

    def test_3(self):
        nums1 = [-1, -1]
        nums2 = [1, 1]
        self.assertEqual(-1, self.max_dot_product(nums1, nums2))
