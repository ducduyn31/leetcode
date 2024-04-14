import unittest
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            if i == 0:
                result.append(0)
                continue
            pos = i >> 1
            result.append(result[pos] + i % 2)

        return result


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.count_bits = Solution().countBits

    def test_count_bits_should_return_0_1_1_given_2(self):
        self.assertEqual([0, 1, 1], self.count_bits(2))

    def test_count_bits_should_return_0_1_1_2_1_2_given_5(self):
        self.assertEqual([0, 1, 1], self.count_bits(2))

    def test_count_bits_should_return_0_1_given_1(self):
        self.assertEqual([0, 1], self.count_bits(1))

    def test_count_bits_should_return_empty_given_0(self):
        self.assertEqual([0], self.count_bits(0))
