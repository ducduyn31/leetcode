import unittest


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            if i % m == 0:
                ans -= i
            else:
                ans += i

        return ans


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.difference_of_sums = Solution().differenceOfSums

    def test_1(self):
        n = 10
        m = 3
        self.assertEqual(19, self.difference_of_sums(n, m))

    def test_2(self):
        n = 5
        m = 6
        self.assertEqual(15, self.difference_of_sums(n, m))

    def test_3(self):
        n = 5
        m = 1
        self.assertEqual(-15, self.difference_of_sums(n, m))
