import math
import unittest
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        freq = sorted(counter.values())
        n = len(freq)

        res = math.inf
        left_sum = 0

        for i in range(n):
            deletions = left_sum
            for j in range(n - 1, i, -1):
                if freq[i] + k >= freq[j]:
                    break
                deletions += freq[j] - freq[i] - k
            res = min(res, deletions)
            left_sum += freq[i]

        return res


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.minimum_deletions = Solution().minimumDeletions

    def test_1(self):
        s = "aabcaba"
        k = 0
        self.assertEqual(
            3,
            self.minimum_deletions(s, k),
        )

    def test_2(self):
        s = "dabdcbdcdcd"
        k = 2
        self.assertEqual(
            2,
            self.minimum_deletions(s, k),
        )

    def test_3(self):
        s = "aaabaaa"
        k = 2
        self.assertEqual(
            1,
            self.minimum_deletions(s, k),
        )
