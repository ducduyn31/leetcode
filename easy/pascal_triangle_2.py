import unittest
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for i in range(1, rowIndex + 1):
            ans.append(ans[-1] * (rowIndex - i + 1) // i)

        return ans


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.get_row = Solution().getRow

    def test_1(self):
        self.assertEqual([1, 3, 3, 1], self.get_row(3))

    def test_2(self):
        self.assertEqual([1], self.get_row(0))

    def test_3(self):
        self.assertEqual([1, 1], self.get_row(1))
