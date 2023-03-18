from typing import List


def numIslands(grid: List[List[str]]) -> int:
    visited = [[False for _ in row] for row in grid]
    count = 0

    def dfs(r, c, max_r, max_c):
        S = [(r, c)]
        while S:
            current_row, current_col = S.pop()
            visited[current_row][current_col] = True
            if current_row > 0 \
                    and not visited[current_row - 1][current_col] \
                    and grid[current_row - 1][current_col] == '1':
                S.append((current_row - 1, current_col))
            if current_col < max_c \
                    and not visited[current_row][current_col + 1] \
                    and grid[current_row][current_col + 1] == '1':
                S.append((current_row, current_col + 1))
            if current_row < max_r \
                    and not visited[current_row + 1][current_col] \
                    and grid[current_row + 1][current_col] == '1':
                S.append((current_row + 1, current_col))
            if current_col > 0 \
                    and not visited[current_row][current_col - 1] \
                    and grid[current_row][current_col - 1] == '1':
                S.append((current_row, current_col - 1))

    for row in range(len(grid)):
        for col, land_or_water in enumerate(grid[row]):
            if visited[row][col]:
                continue

            if grid[row][col] == '1':
                count += 1
                dfs(row, col, len(grid) - 1, len(grid[0]) - 1)

    return count


if __name__ == '__main__':
    print(numIslands(
        [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]))
    print(numIslands(
        [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]))
    print(numIslands([['1', '1', '1'], ['0', '1', '0'], ['1', '1', '1']]))
