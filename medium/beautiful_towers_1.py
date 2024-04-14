import unittest
from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        dp = [0, maxHeights[0]]
        S = [0]
        for i in range(1, n):
            while S and maxHeights[S[-1]] > maxHeights[i]:
                S.pop()
            last_smallest_index = S[-1] if S else -1
            S.append(i)
            distance = i - last_smallest_index
            dp.append(dp[last_smallest_index + 1] + maxHeights[i] * distance)

        maxHeights = maxHeights[::-1]
        dp2 = [0, maxHeights[0]]
        S = [0]
        for i in range(1, n):
            while S and maxHeights[S[-1]] > maxHeights[i]:
                S.pop()
            last_smallest_index = S[-1] if S else -1
            S.append(i)
            distance = i - last_smallest_index
            dp2.append(dp2[last_smallest_index + 1] + maxHeights[i] * distance)

        dp2 = dp2[::-1]
        for i in range(1, n):
            dp[i] = dp[i] + dp2[i]

        return max(dp)


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.maximum_sum_of_heights = Solution().maximumSumOfHeights

    def test_1(self):
        self.assertEqual(13, self.maximum_sum_of_heights([5, 3, 4, 1, 1]))

    def test_2(self):
        self.assertEqual(22, self.maximum_sum_of_heights([6, 5, 3, 9, 2, 7]))

    def test_3(self):
        self.assertEqual(18, self.maximum_sum_of_heights([3, 2, 5, 5, 2, 3]))

    def test_4(self):
        self.assertEqual(100000, self.maximum_sum_of_heights([100000]))
