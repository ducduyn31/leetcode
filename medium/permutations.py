import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list(p) for p in permutations(nums)]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.permute = Solution().permute

    def test_permute_should_return_6_elements(self):
        actual = self.permute([1, 2, 3])
        self.assertCountEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], actual)

    def test_permute_should_return_2_elements(self):
        actual = self.permute([0, 1])
        self.assertCountEqual([[0, 1], [1, 0]], actual)

    def test_permute_should_return_1_element(self):
        actual = self.permute([1])
        self.assertCountEqual([[1]], actual)
