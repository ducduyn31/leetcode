import unittest


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        if n % 3 == 0:
            return 3 ** (n // 3)

        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4

        return 3 ** (n // 3) * 2


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.integer_break = Solution().integerBreak

    def test_1(self):
        n = 2
        self.assertEqual(1, self.integer_break(n))

    def test_2(self):
        n = 10
        self.assertEqual(36, self.integer_break(n))
