import unittest
from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.full_bloom_flowers = Solution().fullBloomFlowers

    def test_1(self):
        self.assertEqual(
            [1, 2, 2, 2],
            self.full_bloom_flowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]),
        )

    def test_2(self):
        self.assertEqual(
            [2, 2, 1],
            self.full_bloom_flowers([[1, 10], [3, 3]], [3, 3, 2]),
        )
