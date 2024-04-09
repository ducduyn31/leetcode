import unittest
from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0

        for i in range(len(tickets)):
            if i < k:
                count += min(tickets[i], tickets[k])
            elif i > k:
                count += min(tickets[i], tickets[k] - 1)

        return count + tickets[k]


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.time_required_to_buy = Solution().timeRequiredToBuy

    def test_1(self):
        tickets = [2, 3, 2]
        k = 2
        self.assertEqual(self.time_required_to_buy(tickets, k), 6)

    def test_2(self):
        tickets = [5, 1, 1, 1]
        k = 0
        self.assertEqual(self.time_required_to_buy(tickets, k), 8)
