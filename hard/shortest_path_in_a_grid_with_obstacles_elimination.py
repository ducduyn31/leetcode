import unittest
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        path = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(m)]
        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

        Q = deque([(0, 0, k)])
        path[0][0][k] = 0

        def progress_if_block(next_m, next_n, prev_m, prev_n, prev_r):
            next_r = prev_r if grid[next_m][next_n] == 0 else prev_r - 1
            if next_r < 0:
                return
            prev_min_path = min(path[next_m][next_n][next_r:])
            next_min_path = min(prev_min_path, path[prev_m][prev_n][prev_r] + 1)
            if next_min_path >= prev_min_path:
                return
            path[next_m][next_n][next_r] = next_min_path
            Q.append((next_m, next_n, next_r))

        while Q:
            current_m, current_n, remaining_k = Q.popleft()
            visited[current_m][current_n][remaining_k] = True

            if current_m > 0 and not visited[current_m - 1][current_n][remaining_k]:
                progress_if_block(current_m - 1, current_n, current_m, current_n, remaining_k)
            if current_m < m - 1 and not visited[current_m + 1][current_n][remaining_k]:
                progress_if_block(current_m + 1, current_n, current_m, current_n, remaining_k)

            if current_n > 0 and not visited[current_m][current_n - 1][remaining_k]:
                progress_if_block(current_m, current_n - 1, current_m, current_n, remaining_k)
            if current_n < n - 1 and not visited[current_m][current_n + 1][remaining_k]:
                progress_if_block(current_m, current_n + 1, current_m, current_n, remaining_k)

        shortest_path = min(path[-1][-1])

        return shortest_path if shortest_path != float('inf') else -1


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.shortest_path = Solution().shortestPath

    def test_1(self):
        self.assertEqual(6, self.shortest_path([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1))

    def test_2(self):
        self.assertEqual(-1, self.shortest_path([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1))
