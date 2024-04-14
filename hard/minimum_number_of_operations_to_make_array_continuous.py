import unittest
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.min_operations = Solution().minOperations

    def test_1(self):
        self.assertEqual(0, self.min_operations([4, 2, 5, 3]))

    def test_2(self):
        self.assertEqual(1, self.min_operations([1, 2, 3, 5, 6]))

    def test_3(self):
        self.assertEqual(3, self.min_operations([1, 10, 100, 1000]))
