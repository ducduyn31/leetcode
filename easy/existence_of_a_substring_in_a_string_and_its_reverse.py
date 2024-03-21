import unittest


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]

        for i in range(len(s) - 1):
            if s[i:i + 2] in rev:
                return True

        return False


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.isSubstringPresent = Solution().isSubstringPresent

    def test_1(self):
        s = "leetcode"
        self.assertEqual(
            True,
            self.isSubstringPresent(s),
        )

    def test_2(self):
        s = "abcba"
        self.assertEqual(
            True,
            self.isSubstringPresent(s),
        )

    def test_3(self):
        s = "abcd"
        self.assertEqual(
            False,
            self.isSubstringPresent(s),
        )
