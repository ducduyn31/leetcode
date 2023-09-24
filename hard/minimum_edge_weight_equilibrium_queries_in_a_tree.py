import unittest
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        children = defaultdict(list)
        log_height = n.bit_length() + 1
        weights = defaultdict(Counter)
        up = [[-1] * n]

        for u, v, w in edges:
            children[u].append((v, w))
            children[v].append((u, w))

        visited = [False] * n
        level = [-1] * n

        def dfs(node_id, current_level):
            visited[node_id] = True
            level[node_id] = current_level

            for child, cost in children[node_id]:
                if visited[child]:
                    continue
                weights[child] = weights[node_id].copy()
                weights[child].update([cost])
                up[0][child] = node_id
                dfs(child, current_level + 1)

        dfs(0, 0)

        for l in range(1, log_height):
            temp = [-1] * n
            for v in range(n):
                if up[l - 1][v] == -1:
                    continue
                temp[v] = up[l - 1][up[l - 1][v]]
            up.append(temp)

        def lca(node_1, node_2):
            if level[node_1] > level[node_2]:
                node_1, node_2 = node_2, node_1

            k = level[node_2] - level[node_1]

            for log_k in range(log_height - 1, -1, -1):
                if k >= (1 << log_k):
                    node_2 = up[log_k][node_2]
                    k -= 1 << log_k

            while node_1 != node_2:
                node_1 = up[0][node_1]
                node_2 = up[0][node_2]

            return node_1

        ans = []
        for start, end in queries:
            anc = lca(start, end)
            counter = weights[start] + weights[end] - weights[anc] - weights[anc]
            if not counter:
                ans.append(0)
                continue
            _, f = counter.most_common(1)[0]
            ans.append(sum(counter.values()) - f)

        return ans


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.min_operations_queries = Solution().minOperationsQueries

    def test_1(self):
        n = 7
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]]
        queries = [[0, 3], [3, 6], [2, 6], [0, 6]]
        self.assertEqual([0, 0, 1, 3], self.min_operations_queries(n, edges, queries))

    def test_2(self):
        n = 8
        edges = [[1, 2, 6], [1, 3, 4], [2, 4, 6], [2, 5, 3], [3, 6, 6], [3, 0, 8], [7, 0, 2]]
        queries = [[4, 6], [0, 4], [6, 5], [7, 4]]
        self.assertEqual([1, 2, 2, 3], self.min_operations_queries(n, edges, queries))

    def test_3(self):
        n = 1
        edges = []
        queries = [[0, 0]]
        self.assertEqual([0], self.min_operations_queries(n, edges, queries))
