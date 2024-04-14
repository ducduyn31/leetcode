import unittest
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        pass


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.verify_preorder = Solution().verifyPreorder

    def test_1(self):
        preorder = [5, 2, 1, 3, 6]
        self.assertTrue(self.verify_preorder(preorder))

    def test_2(self):
        preorder = [5, 2, 6, 1, 3]
        self.assertFalse(self.verify_preorder(preorder))
