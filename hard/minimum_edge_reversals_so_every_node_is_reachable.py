import unittest
from collections import defaultdict
from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        children = defaultdict(set)
        parents = defaultdict(set)
        visited = [False] * n
        reversals = [0] * n

        for start, end in edges:
            children[start].add(end)
            parents[end].add(start)

        def dfs(node_id: int):
            visited[node_id] = True

            for child_id in children[node_id]:
                if visited[child_id]:
                    continue
                dfs(child_id)

            for parent_id in parents[node_id]:
                if visited[parent_id]:
                    continue
                reversals[0] += 1
                dfs(parent_id)

        dfs(0)

        S = [0]
        visited = [False] * n
        while S:
            current = S.pop()
            visited[current] = True
            for child_id in children[current]:
                if visited[child_id]:
                    continue
                reversals[child_id] = reversals[current] + 1
                S.append(child_id)
            for parent_id in parents[current]:
                if visited[parent_id]:
                    continue
                reversals[parent_id] = reversals[current] - 1
                S.append(parent_id)

        return reversals


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.min_edge_reversals = Solution().minEdgeReversals

    def test_1(self) -> None:
        self.assertEqual([1, 1, 0, 2], self.min_edge_reversals(4, [[2, 0], [2, 1], [1, 3]]))

    def test_2(self) -> None:
        self.assertEqual([2, 0, 1], self.min_edge_reversals(3, [[1, 2], [2, 0]]))

    def test_3(self) -> None:
        self.assertEqual([2, 3, 0, 1], self.min_edge_reversals(4, [[0, 1], [3, 0], [2, 3]]))

    def test_4(self) -> None:
        self.assertEqual([2, 1, 2, 3], self.min_edge_reversals(4, [[0, 3], [1, 2], [2, 3]]))
