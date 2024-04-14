import unittest


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 4 != 0:
                return False
            n >>= 2

        return True


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.is_power_of_four = Solution().isPowerOfFour

    def test_1(self):
        n = 16

        self.assertTrue(self.is_power_of_four(n))

    def test_2(self):
        n = 5

        self.assertFalse(self.is_power_of_four(n))

    def test_3(self):
        n = 1

        self.assertTrue(self.is_power_of_four(n))

    def test_4(self):
        n = 0
        self.assertFalse(self.is_power_of_four(n))
