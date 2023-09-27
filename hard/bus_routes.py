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

        source_nodes = [node_id for node_id in range(n) if source in routes[node_id]]
        target_nodes = [node_id for node_id in range(n) if target in routes[node_id]]
        visited = [False] * n
        S = source_nodes[:]

        while S:
            current_node = S.pop()
            visited[current_node] = True

            for node_id in range(n):
                if visited[node_id]:
                    continue
                if routes[current_node].intersection(routes[node_id]):
                    children[current_node].add(node_id)
                    children[node_id].add(current_node)
                    S.append(node_id)

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
