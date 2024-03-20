import unittest


class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix_suffix_end = [0] * len(s)
        i, len_last_prefix_suffix = 1, 0

        while i < len(s):
            if s[i] == s[len_last_prefix_suffix]:
                len_last_prefix_suffix += 1
                prefix_suffix_end[i] = len_last_prefix_suffix
                i += 1
            elif len_last_prefix_suffix == 0:
                i += 1
                len_last_prefix_suffix = 0
            else:
                len_last_prefix_suffix = prefix_suffix_end[len_last_prefix_suffix - 1]

        return s[:prefix_suffix_end[-1]]


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.longest_prefix = Solution().longestPrefix

    def test_1(self):
        s = "level"
        self.assertEqual(
            "l",
            self.longest_prefix(s),
        )

    def test_2(self):
        s = "ababab"
        self.assertEqual(
            "abab",
            self.longest_prefix(s),
        )

    def test_3(self):
        s = "leetcodeleet"
        self.assertEqual(
            "leet",
            self.longest_prefix(s),
        )

    def test_4(self):
        s = "a"
        self.assertEqual(
            "",
            self.longest_prefix(s),
        )
