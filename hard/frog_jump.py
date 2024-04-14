import unittest
from functools import cache
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)

        @cache
        def jump(pos: int, step: int):
            if pos not in stone_set:
                return False
            if pos == stones[-1]:
                return True

            steps = [step - 1, step, step + 1]

            return any(jump(pos + k, k) for k in steps if pos + k > pos)

        return jump(0, 0)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.can_cross = Solution().canCross

    def test_1(self):
        self.assertTrue(self.can_cross([0, 1, 3, 5, 6, 8, 12, 17]))

    def test_2(self):
        self.assertFalse(self.can_cross([0, 1, 2, 3, 4, 8, 9, 11]))
