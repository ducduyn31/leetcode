import unittest
from collections import Counter
from math import inf
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections = {}

        for a, b in roads:
            connections[a] = connections[a] if a in connections else set()
            connections[b] = connections[b] if b in connections else set()
            connections[a].add(b)
            connections[b].add(a)

        max_rank = 0

        for first in connections:
            for second in connections:
                if first == second:
                    continue
                rank = len(connections[first]) + len(connections[second])
                if second in connections[first]:
                    rank -= 1

                max_rank = max(max_rank, rank)

        return max_rank


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.maximal_network_rank = Solution().maximalNetworkRank

    def test_maximal_network_rank_should_return_4_given_n_4(self):
        n = 4
        roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
        self.assertEqual(4, self.maximal_network_rank(n, roads))

    def test_maximal_network_rank_should_return_5_given_n_5(self):
        n = 5
        roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
        self.assertEqual(5, self.maximal_network_rank(n, roads))

    def test_maximal_network_rank_should_return_5_given_n_8(self):
        n = 8
        roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        self.assertEqual(5, self.maximal_network_rank(n, roads))
