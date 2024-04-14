import unittest
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        sub = 0
        max_val = 0

        for x in nums:
            ans = max(ans, sub * x)
            sub = max(sub, max_val - x)
            max_val = max(max_val, x)

        return ans


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.maximum_triplet_value = Solution().maximumTripletValue

    def test_1(self):
        self.assertEqual(self.maximum_triplet_value([12, 6, 1, 2, 7]), 77)

    def test_2(self):
        self.assertEqual(self.maximum_triplet_value([1, 10, 3, 4, 19]), 133)

    def test_3(self):
        self.assertEqual(self.maximum_triplet_value([1, 2, 3]), 0)
