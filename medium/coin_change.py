import unittest
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        min_number_of_coins = [-1 for _ in range(amount + 1)]

        for sub_amount in range(1, amount + 1):
            if sub_amount in coins:
                min_number_of_coins[sub_amount] = 1
            else:
                prev_states = [
                    min_number_of_coins[sub_amount - coin_value]
                    for coin_value in coins
                    if coin_value <= sub_amount and
                       min_number_of_coins[sub_amount - coin_value] > -1
                ]
                if not prev_states:
                    continue
                min_number_of_coins[sub_amount] = min(prev_states) + 1

        return min_number_of_coins[-1]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.coin_change = Solution().coinChange

    def test_coin_change_should_return_5(self):
        self.assertEqual(5, self.coin_change([2, 4, 5], 21))

    def test_coin_change_should_return_3(self):
        self.assertEqual(3, self.coin_change([1, 2, 3, 5], 11))

    def test_coin_change_should_return_0(self):
        self.assertEqual(0, self.coin_change([2], 0))

    def test_coin_change_should_return_minus_1(self):
        self.assertEqual(-1, self.coin_change([2], 3))
