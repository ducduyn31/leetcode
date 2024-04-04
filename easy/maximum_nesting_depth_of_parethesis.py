import unittest


class Solution:
    def maxDepth(self, s: str) -> int:
        max_level = opens = 0

        for c in s:
            if c == "(":
                opens += 1
                max_level = max(max_level, opens)
            elif c == ")":
                opens -= 1

        return max_level


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.max_depth = Solution().maxDepth

    def test_1(self):
        s = "(1+(2*3)+((8)/4))+1"
        self.assertEqual(3, self.max_depth(s))

    def test_2(self):
        s = "(1)+((2))+(((3)))"
        self.assertEqual(3, self.max_depth(s))

    def test_3(self):
        s = "1+(2*3)/(2-1)"
        self.assertEqual(1, self.max_depth(s))
