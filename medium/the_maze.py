import unittest
from collections import deque
from typing import List


class Solution:

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque()
        visited = set()
        q.append(start)

        def left(row, col):
            while col > 0:
                col -= 1
                if maze[row][col] == 1:
                    return row, col + 1

            return row, col

        def right(row, col):
            while col < len(maze[0]) - 1:
                col += 1
                if maze[row][col] == 1:
                    return row, col - 1

            return row, col

        def up(row, col):
            while row > 0:
                row -= 1
                if maze[row][col] == 1:
                    return row + 1, col

            return row, col

        def down(row, col):
            while row < len(maze) - 1:
                row += 1
                if maze[row][col] == 1:
                    return row - 1, col

            return row, col

        while q:
            row, col = q.popleft()

            if row == destination[0] and col == destination[1]:
                return True

            visited.add((row, col))
            l, r, u, d = left(row, col), right(row, col), up(row, col), down(row, col)
            if l not in visited:
                q.append(l)
            if r not in visited:
                q.append(r)
            if u not in visited:
                q.append(u)
            if d not in visited:
                q.append(d)

        return False


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.has_path = Solution().hasPath

    def test_has_path_should_return_true_case_1(self):
        maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        start = [0, 4]
        destination = [4, 4]
        self.assertTrue(self.has_path(maze, start, destination))

    def test_has_path_should_return_false_case_2(self):
        maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        start = [0, 4]
        destination = [3, 2]
        self.assertFalse(self.has_path(maze, start, destination))

    def test_has_path_should_return_false_case_3(self):
        maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
        start = [4, 3]
        destination = [0, 1]
        self.assertFalse(self.has_path(maze, start, destination))
