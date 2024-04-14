import unittest


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = s.count(c)

        return n * (n - 1) // 2 + n


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.count_substrings = Solution().countSubstrings

    def test_1(self):
        s = "abada"
        c = "a"
        self.assertEqual(
            6,
            self.count_substrings(s, c),
        )

    def test_2(self):
        s = "zzz"
        c = "z"
        self.assertEqual(
            6,
            self.count_substrings(s, c),
        )
