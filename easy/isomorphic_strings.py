import unittest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = [-1] * 256

        for i in range(len(s)):
            if mapper[ord(s[i])] == -1:
                mapper[ord(s[i])] = ord(t[i])
            elif mapper[ord(s[i])] != ord(t[i]):
                return False

        return len(set(s)) == len(set(t))


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.is_isomorphic = Solution().isIsomorphic

    def test_1(self):
        s = "egg"
        t = "add"
        self.assertEqual(True, self.is_isomorphic(s, t))

    def test_2(self):
        s = "foo"
        t = "bar"
        self.assertEqual(False, self.is_isomorphic(s, t))
