import unittest
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        routes = [set(r) for r in routes]
        n = len(routes)
        children = defaultdict(set)

        for node_id in range(n):
            for other_node_id in range(node_id + 1, n):
                if routes[node_id].intersection(routes[other_node_id]):
                    children[node_id].add(other_node_id)
                    children[other_node_id].add(node_id)

        source_nodes = set()
        target_nodes = set()

        for node_id in range(n):
            if source in routes[node_id]:
                source_nodes.add(node_id)
            if target in routes[node_id]:
                target_nodes.add(node_id)

        visited = [False] * n

        Q = deque([(node_id, 1) for node_id in source_nodes])
        while Q:
            current_node, dist = Q.popleft()
            visited[current_node] = True

            if current_node in target_nodes:
                return dist

            for child in children[current_node]:
                if visited[child]:
                    continue
                Q.append((child, dist + 1))

        return -1


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.num_buses_to_destination = Solution().numBusesToDestination

    def test_1(self):
        self.assertEqual(2, self.num_buses_to_destination([[1, 2, 7], [3, 6, 7]], 1, 6))

    def test_2(self):
        self.assertEqual(-1, self.num_buses_to_destination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12))

    def test_3(self):
        self.assertEqual(0, self.num_buses_to_destination([[1, 7], [3, 5]], 5, 5))
