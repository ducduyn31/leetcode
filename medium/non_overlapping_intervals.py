import unittest
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:



class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.erase_overlap_intervals = Solution().eraseOverlapIntervals

    def test_1(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(
            1,
            self.erase_overlap_intervals(intervals),
        )

    def test_2(self):
        intervals = [[1, 2], [1, 2], [1, 2]]
        self.assertEqual(
            2,
            self.erase_overlap_intervals(intervals),
        )

    def test_3(self):
        intervals = [[1, 2], [2, 3]]
        self.assertEqual(
            0,
            self.erase_overlap_intervals(intervals),
        )
