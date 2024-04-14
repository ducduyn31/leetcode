import unittest
from typing import List


class Solution:

    def __init__(self):
        self.visited = None
        self.height = 0
        self.width = 0
        self.x = 0
        self.x_inc = 1
        self.y = 0
        self.y_inc = 0

    def solve(self, board: List[List[str]]) -> None:
        self.height, self.width = len(board), len(board[0])
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

        def dfs_O(x, y):
            if self.visited[y][x]:
                return
            self.visited[y][x] = True

            if board[y][x] == 'X':
                return

            if x < self.width - 1:
                dfs_O(x + 1, y)
            if x > 0:
                dfs_O(x - 1, y)
            if y < self.height - 1:
                dfs_O(x, y + 1)
            if y > 0:
                dfs_O(x, y - 1)

        for _ in range((self.width + self.height - 2) * 2):
            dfs_O(self.x, self.y)
            self.inc()

        for y in range(1, self.height -1):
            for x in range(1, self.width - 1):
                if self.visited[y][x]:
                    continue

                self.visited[y][x] = True
                board[y][x] = 'X'

    def inc(self):
        if self.x == 0 and self.y == 0:
            self.x_inc = 1
            self.y_inc = 0
        elif self.x == self.width - 1 and self.y == 0:
            self.x_inc = 0
            self.y_inc = 1
        elif self.x == self.width - 1 and self.y == self.height - 1:
            self.x_inc = -1
            self.y_inc = 0
        elif self.x == 0 and self.y == self.height - 1:
            self.x_inc = 0
            self.y_inc = -1

        self.x += self.x_inc
        self.y += self.y_inc


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.surrounded_regions = Solution().solve

    def test_surrounded_regions_should_replace_O_with_X(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]

        self.surrounded_regions(board)

        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"]
        ]
        self.assertEqual(expected, board)

    def test_surrounded_regions_should_replace_some(self):
        board = [
            ["X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X"]
        ]

        self.surrounded_regions(board)

        expected = [
            ["X", "O", "X", "O", "X", "O"],
            ["O", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "O"],
            ["O", "X", "O", "X", "O", "X"]
        ]

    def test_surrounded_regions_should_replace_some_2(self):
        board = [
            ["O", "X", "X", "O", "X"],
            ["X", "O", "O", "X", "O"],
            ["X", "O", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"]
        ]

        self.surrounded_regions(board)

        expected = [
            ["O", "X", "X", "O", "X"],
            ["X", "X", "X", "X", "O"],
            ["X", "X", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"]
        ]

        self.assertEqual(expected, board)

    def test_surrounded_regions_should_skip(self):
        board = [["X"]]
        self.surrounded_regions(board)
        expected = [["X"]]
        self.assertEqual(expected, board)
