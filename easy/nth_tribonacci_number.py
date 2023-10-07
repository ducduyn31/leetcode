import unittest


class Solution:
    def tribonacci(self, n: int) -> int:
        t_prev, t_mid, t_last = 0, 1, 1

        if n == 0:
            return t_prev
        if n == 1:
            return t_mid
        if n == 2:
            return t_last

        for _ in range(2, n):
            t_prev, t_mid, t_last = t_mid, t_last, t_prev + t_mid + t_last

        return t_last


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.tribonacci = Solution().tribonacci

    def test_1(self):
        n = 4
        self.assertEqual(4, self.tribonacci(n))

    def test_2(self):
        n = 25
        self.assertEqual(1389537, self.tribonacci(n))
