import unittest
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        match_values = defaultdict(int)
        count = 0

        for x1, y1 in coordinates:
            if (x1, y1) in match_values:
                count += match_values[x1, y1]

            for x in range(k + 1):
                match_x = x ^ x1
                match_y = (k - x) ^ y1

                match_values[match_x, match_y] += 1

        return count


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.count_pairs = Solution().countPairs

    def test_1(self):
        self.assertEqual(2, self.count_pairs([[1, 2], [4, 2], [1, 3], [5, 2]], 5))

    def test_2(self):
        self.assertEqual(10, self.count_pairs([[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], 0))
