import math
import unittest


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        lsp = [0] * len(word)
        longest_prefix = 0
        i = 1

        while i < len(word):
            if word[i] == word[longest_prefix]:
                longest_prefix += 1
                lsp[i] = longest_prefix
                i += 1
            elif longest_prefix == 0:
                lsp[i] = 0
                i += 1
            else:
                longest_prefix = lsp[longest_prefix - 1]

        for i in range(k, len(lsp), k):
            remaining = len(lsp) - i
            end = 2 * i - 1
            if k > remaining and lsp[-1] == remaining:
                return i // k
            elif end <= len(lsp) and lsp[end] == i:
                return i // k

        return math.ceil(len(word) / k)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.minimum_time_to_initial_state = Solution().minimumTimeToInitialState

    def test_1(self):
        word = "abacaba"
        k = 3
        self.assertEqual(2, self.minimum_time_to_initial_state(word, k))

    def test_2(self):
        word = "abacaba"
        k = 4
        self.assertEqual(1, self.minimum_time_to_initial_state(word, k))

    def test_3(self):
        word = "abcbabcd"
        k = 2
        self.assertEqual(4, self.minimum_time_to_initial_state(word, k))
