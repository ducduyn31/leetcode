import unittest
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.candy = Solution().candy

    def test_1(self):
        self.assertEqual(5, self.candy([1, 0, 2]))

    def test_2(self):
        self.assertEqual(4, self.candy([1, 2, 2]))

    def test_3(self):
        self.assertEqual(7, self.candy([1, 3, 2, 2, 1]))

    def test_4(self):
        self.assertEqual(110, self.candy([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]))

    def test_5(self):
        self.assertEqual(11, self.candy([1, 3, 4, 5, 2]))
