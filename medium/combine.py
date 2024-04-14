import unittest
from collections import Counter
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combination(n, k, 1)

    def combination(self, n: int, k: int, start: int) -> List[List[int]]:
        result = []
        if k == 1:
            return [[i] for i in range(start, n + 1)]

        for i in range(start, n - k + 2):
            for c in self.combination(n, k - 1, i + 1):
                c.append(i)
                result.append(c)
        return result


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.combine = Solution().combine

    def assertNestedCountEqual(self, expected: List[List], actual: List[List]):
        expected_with_counter = [Counter(el) for el in expected]
        actual_with_counter = [Counter(el) for el in actual]
        return self.assertCountEqual(expected_with_counter, actual_with_counter)

    def test_combine_should_return_1_given_1(self):
        actual = self.combine(1, 1)
        self.assertNestedCountEqual([[1]], actual)

    def test_combine_should_return_2_given_2_1(self):
        actual = self.combine(2, 1)
        self.assertNestedCountEqual([[1], [2]], actual)

    def test_combine_should_return_3_given_3_2(self):
        actual = self.combine(3, 2)
        self.assertNestedCountEqual([[1, 2], [1, 3], [2, 3]], actual)

    def test_combine_should_return_6_given_4_2(self):
        actual = self.combine(4, 2)
        self.assertNestedCountEqual([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], actual)
