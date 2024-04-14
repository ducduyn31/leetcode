import unittest
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        transactions = []

        start = end = 0
        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                end = i
                continue
            if end > start:
                transactions.append((start, end))
            start = i

        if end > start:
            transactions.append((start, end))

        while len(transactions) > k:
            min_lost_remove_idx = -1
            min_lost_remove = float('inf')
            min_lost_merge_idx = -1
            min_lost_merge = float('inf')
            for i in range(len(transactions) - 1):
                start, end = transactions[i]
                next_start, next_end = transactions[i + 1]
                value = prices[end] - prices[start]
                next_value = prices[next_end] - prices[next_start]
                merge_value = prices[next_end] - prices[start]

                if value < min_lost_remove:
                    min_lost_remove_idx = i
                    min_lost_remove = value

                if value + next_value - merge_value < min_lost_merge:
                    min_lost_merge_idx = i
                    min_lost_merge = value + next_value - merge_value

            s_last, e_last = transactions[-1]
            value_last = prices[e_last] - prices[s_last]
            if value_last < min_lost_remove:
                min_lost_remove_idx = len(transactions) - 1
                min_lost_remove = value_last

            if min_lost_merge < min_lost_remove:
                _, e2 = transactions.pop(min_lost_merge_idx + 1)
                s1, _ = transactions[min_lost_merge_idx]
                transactions[min_lost_merge_idx] = (s1, e2)
            else:
                transactions.pop(min_lost_remove_idx)

        return sum(prices[e] - prices[s] for s, e in transactions)


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.max_profit = Solution().maxProfit

    def test_1(self) -> None:
        self.assertEqual(2, self.max_profit(2, [2, 4, 1]))

    def test_2(self) -> None:
        self.assertEqual(7, self.max_profit(2, [3, 2, 6, 5, 0, 3]))

    def test_3(self) -> None:
        self.assertEqual(3, self.max_profit(2, [1, 2, 4]))

    def test_4(self) -> None:
        self.assertEqual(6, self.max_profit(2, [3, 3, 5, 0, 0, 3, 1, 4]))

    def test_5(self) -> None:
        self.assertEqual(15, self.max_profit(4, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
