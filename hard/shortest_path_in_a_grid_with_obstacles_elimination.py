import heapq
import unittest
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = {(0, 0, k)}

        def distance(row, col):
            return (rows - row) + (cols - col) - 2

        Q = [(distance(0, 0), 0, (0, 0, k))]

        while Q:
            estimation_dist, steps, (current_row, current_col, remaining_k) = heapq.heappop(Q)

            if estimation_dist - steps <= remaining_k:
                return estimation_dist

            for next_row, next_col in [(current_row - 1, current_col), (current_row + 1, current_col),
                                       (current_row, current_col - 1), (current_row, current_col + 1)]:

                if 0 <= next_row < rows and 0 <= next_col < cols:
                    next_k = remaining_k - grid[next_row][next_col]

                    if next_k >= 0 and (next_row, next_col, next_k) not in visited:
                        visited.add((next_row, next_col, next_k))
                        heapq.heappush(Q, (
                            distance(next_row, next_col) + steps + 1, steps + 1, (next_row, next_col, next_k)))

        return -1


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.shortest_path = Solution().shortestPath

    def test_1(self):
        self.assertEqual(6, self.shortest_path([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1))

    def test_2(self):
        self.assertEqual(-1, self.shortest_path([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1))
