import unittest
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        children = defaultdict(set)
        for u, v in edges:
            children[u].add(v)
            children[v].add(u)

        ans = [0]

        def dfs(node_id, parent):
            node_is_prime = int(is_prime[node_id])
            path_with_prime, path_no_prime = node_is_prime, 1 - node_is_prime

            for child in children[node_id]:
                if child == parent:
                    continue
                neighbor_with_prime, neighbor_no_prime = dfs(child, node_id)
                ans[0] += path_with_prime * neighbor_no_prime + path_no_prime * neighbor_with_prime
                if is_prime[node_id]:
                    path_with_prime += neighbor_no_prime
                else:
                    path_with_prime += neighbor_with_prime
                    path_no_prime += neighbor_no_prime

            return path_with_prime, path_no_prime

        dfs(1, 0)
        return ans[0]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.count_paths = Solution().countPaths

    def test_1(self):
        n = 5
        edges = [[1, 2], [1, 3], [2, 4], [2, 5]]
        self.assertEqual(4, self.count_paths(n, edges))

    def test_2(self):
        n = 6
        edges = [[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]]
        self.assertEqual(6, self.count_paths(n, edges))
