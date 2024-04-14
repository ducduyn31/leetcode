import unittest
from collections import Counter
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one_count = Counter(data).get(1)

        if not one_count:
            return 0

        start, end = 0, 0
        current_zero = 0
        min_swap = one_count

        while end < len(data):
            while end - start < one_count:
                if data[end] == 0:
                    current_zero += 1
                end += 1

            min_swap = min(min_swap, current_zero)
            if data[start] == 0:
                current_zero -= 1
            start += 1

        return min_swap


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.min_swaps = Solution().minSwaps

    def test_should_return_1_given_1_0_1_0_1(self):
        self.assertEqual(1, self.min_swaps([1, 0, 1, 0, 1]))

    def test_should_return_0_given_0_0_0_1_0(self):
        self.assertEqual(0, self.min_swaps([0, 0, 0, 1, 0]))

    def test_should_return_0_given_0_0_0_0_0(self):
        self.assertEqual(0, self.min_swaps([0, 0, 0, 0, 0]))

    def test_should_return_3_given_1_0_1_0_1_0_0_1_1_0_1(self):
        self.assertEqual(3, self.min_swaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))
