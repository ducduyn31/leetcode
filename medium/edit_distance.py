import unittest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + 1
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.min_distance = Solution().minDistance

    def test_edit_distance_should_return_3(self):
        self.assertEqual(3, self.min_distance("horse", "ros"))

    def test_edit_distance_should_return_5(self):
        self.assertEqual(5, self.min_distance("intention", "execution"))

    def test_edit_distance_should_return_2(self):
        self.assertEqual(2, self.min_distance("sea", "eat"))
