from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def dfs(r: int, c: int, origin_color: int, new_color: int):
        if image[r][c] != origin_color:
            return
        image[r][c] = new_color

        if r >= 1:
            dfs(r - 1, c, origin_color, new_color)
        if c >= 1:
            dfs(r, c - 1, origin_color, new_color)
        if r + 1 < len(image):
            dfs(r + 1, c, origin_color, new_color)
        if c + 1 < len(image[0]):
            dfs(r, c + 1, origin_color, new_color)

    if image[sr][sc] != newColor:
        dfs(sr, sc, origin_color=image[sr][sc], new_color=newColor)

    return image


if __name__ == '__main__':
    assert floodFill([[0, 1, 0], [0, 0, 1]], 1, 1, 1) == [[1, 1, 0], [1, 1, 1]]
    assert floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
