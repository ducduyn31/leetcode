from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

    def dfs(row: int, column: int, original: int):
        if row < 0 or row >= len(image) or column < 0 or column >= len(image[0]):
            return

        if visited[row][column]:
            return

        if image[row][column] != original and image[row][column] != newColor:
            return

        new_original = image[row][column]
        image[row][column] = newColor
        visited[row][column] = True

        dfs(row - 1, column, new_original)
        dfs(row, column - 1, new_original)
        dfs(row + 1, column, new_original)
        dfs(row, column + 1, new_original)

    dfs(sr, sc, image[sr][sc])

    return image


if __name__ == '__main__':
    print(floodFill([[0, 1, 0], [0, 0, 1]], 1, 1, 1))
    print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
