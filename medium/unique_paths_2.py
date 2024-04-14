import unittest
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col]:
                    paths[row][col] = 0
                elif row == 0 and col == 0:
                    paths[row][col] = 1
                elif row == 0:
                    paths[row][col] = min(paths[row][col - 1], 1)
                elif col == 0:
                    paths[row][col] = min(paths[row - 1][col], 1)
                else:
                    paths[row][col] = paths[row][col - 1] + paths[row - 1][col]

        return paths[-1][-1]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.unique_paths = Solution().uniquePathsWithObstacles

    def test_unique_paths_should_return_2_given_grid_3x3(self):
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(2, self.unique_paths(obstacleGrid))

    def test_unique_paths_should_return_1_given_grid_2x2(self):
        obstacleGrid = [[0, 1], [0, 0]]
        self.assertEqual(1, self.unique_paths(obstacleGrid))
