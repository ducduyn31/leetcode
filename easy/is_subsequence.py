import unittest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr, t_ptr = 0, 0
        s_n, t_n = len(s), len(t)

        if s_n == 0:
            return True

        if s_n > t_n:
            return False

        while t_ptr < t_n and s_ptr < s_n:
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1

        return s_ptr == s_n


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.is_subsequence = Solution().isSubsequence

    def test_1(self):
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(self.is_subsequence(s, t))

    def test_2(self):
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(self.is_subsequence(s, t))

    def test_3(self):
        s = ""
        t = "ahbgdc"
        self.assertTrue(self.is_subsequence(s, t))

    def test_4(self):
        s = "b"
        t = "abc"
        self.assertTrue(self.is_subsequence(s, t))
