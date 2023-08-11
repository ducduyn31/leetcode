import unittest
from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        @cache
        def dp(sub_amount: int, coin_count: int):
            if sub_amount <= 0 or coin_count == 0:
                return 0

            last_coin = coins[coin_count - 1]

            with_out_last_coin = dp(sub_amount, coin_count - 1)
            only_last_coin = int(sub_amount == last_coin)
            with_last_coin = dp(sub_amount - last_coin, coin_count)

            return with_out_last_coin + only_last_coin + with_last_coin

        return dp(amount, len(coins))


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.change = Solution().change

    def test_change_should_return_1_given_amount_5(self):
        coins = [1]
        amount = 5
        self.assertEqual(1, self.change(amount, coins))

    def test_change_should_return_4_given_amount_5(self):
        coins = [1, 2, 5]
        amount = 5
        self.assertEqual(4, self.change(amount, coins))

    def test_change_should_return_0_given_amount_3(self):
        coins = [2]
        amount = 3
        self.assertEqual(0, self.change(amount, coins))

    def test_change_should_return_1_given_amount_10(self):
        coins = [10]
        amount = 10
        self.assertEqual(1, self.change(amount, coins))

    def test_change_should_return_1_given_amount_0(self):
        coins = [7]
        amount = 0
        self.assertEqual(1, self.change(amount, coins))
