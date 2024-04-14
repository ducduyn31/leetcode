import unittest
from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        Q = deque([0])
        visited = set()

        while Q:
            current = Q.popleft()
            visited.add(current)
            neighbors = graph[current]
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                Q.append(neighbor)

        return 0


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.shortest_path_length = Solution().shortestPathLength

    def test_1(self) -> None:
        self.assertEqual(self.shortest_path_length([[1, 2, 3], [0], [0], [0]]), 4)

    def test_2(self) -> None:
        self.assertEqual(self.shortest_path_length([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]), 4)
