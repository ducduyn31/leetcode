import unittest


class Solution:
    def countOrders(self, n: int) -> int:
        mod = 1_000_000_007
        res = 1

        for i in range(2, n + 1):
            res *= i*(2*i - 1)
        return res % mod


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.count_orders = Solution().countOrders

    def test_count_orders_should_return_1_given_1(self):
        self.assertEqual(1, self.count_orders(1))

    def test_count_orders_should_return_1_given_2(self):
        self.assertEqual(6, self.count_orders(2))

    def test_count_orders_should_return_1_given_3(self):
        self.assertEqual(90, self.count_orders(3))
