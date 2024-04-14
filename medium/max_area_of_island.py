from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    def dfs(x: int, y: int):
        if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
            return 0

        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0

        left = dfs(x, y - 1)
        right = dfs(x, y + 1)
        up = dfs(x - 1, y)
        down = dfs(x + 1, y)

        return 1 + left + right + up + down

    max_area = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            max_area = max(max_area, dfs(i, j))

    return max_area


if __name__ == '__main__':
    assert maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6

    assert maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
