import unittest


class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        s = list(s)
        while i < len(s) - 1:
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                i = max(0, i - 1)
            else:
                i += 1

        return "".join(s)




class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.make_good = Solution().makeGood

    def test_1(self):
        s = "leEeetcode"
        self.assertEqual("leetcode", self.make_good(s))

    def test_2(self):
        s = "abBAcC"
        self.assertEqual("", self.make_good(s))

    def test_3(self):
        s = "s"
        self.assertEqual("s", self.make_good(s))
