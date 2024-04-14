import unittest
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n + 1)

        for i in range(n+1):
            start = max(i - ranges[i], 0)
            end = i + ranges[i]
            max_reach[start] = max(max_reach[start], end)

        last_reach = next_reach = 0
        count = 0

        for i in range(n+1):
            if i > next_reach:
                return -1

            if i > last_reach:
                count += 1
                last_reach = next_reach

            next_reach = max(next_reach, max_reach[i])

        return count


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.min_taps = Solution().minTaps

    def test_1(self):
        n = 5
        ranges = [3, 4, 1, 1, 0, 0]
        self.assertEqual(1, self.min_taps(n, ranges))

    def test_2(self):
        n = 3
        ranges = [0, 0, 0, 0]
        self.assertEqual(-1, self.min_taps(n, ranges))

    def test_3(self):
        n = 7
        ranges = [1, 2, 1, 0, 2, 1, 0, 1]
        self.assertEqual(3, self.min_taps(n, ranges))
