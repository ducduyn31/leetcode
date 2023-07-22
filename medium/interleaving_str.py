import unittest


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [False for _ in range(len(s2) + 1)]
        dp[0] = True

        for x in range(len(s1) + 1):
            for y in range(len(s2) + 1):
                if x == y == 0:
                    continue
                if y == 0:
                    dp[0] = dp[0] and s1[x - 1] == s3[x - 1]
                elif x == 0:
                    dp[y] = dp[y - 1] and s2[y - 1] == s3[y - 1]
                else:
                    dp[y] = (dp[y - 1] and s3[x + y - 1] == s2[y - 1]) or (
                                dp[y] and s3[x + y - 1] == s1[x - 1])

        return dp[-1]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.is_interleave = Solution().isInterleave

    def test_is_interleave_should_return_true_given_aadbbcbcac(self):
        self.assertTrue(self.is_interleave('aabcc', 'dbbca', 'aadbbcbcac'))

    def test_is_interleave_should_return_false_given_aadbbbaccc(self):
        self.assertFalse(self.is_interleave('aabcc', 'dbbca', 'aadbbbaccc'))

    def test_is_interleave_should_return_true_given_empty_str(self):
        self.assertTrue(self.is_interleave('', '', ''))
