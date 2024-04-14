import unittest
from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = Counter(s)
        return "1" * (counter["1"] - 1) + "0" * counter["0"] + "1"


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.maximum_odd_binary_number = Solution().maximumOddBinaryNumber

    def test_1(self) -> None:
        self.assertEqual("001", self.maximum_odd_binary_number("010"))

    def test_2(self) -> None:
        self.assertEqual("1001", self.maximum_odd_binary_number("0101"))
