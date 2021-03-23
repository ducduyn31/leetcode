from typing import List


def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)

    def swap_four(matrix: List[List[int]], pos1, pos2, pos3, pos4) -> None:
        matrix[pos1[0]][pos1[1]], matrix[pos2[0]][pos2[1]], matrix[pos3[0]][pos3[1]], matrix[pos4[0]][pos4[1]] = \
            matrix[pos4[0]][pos4[1]], matrix[pos1[0]][pos1[1]], matrix[pos2[0]][pos2[1]], matrix[pos3[0]][pos3[1]]

    def get_consecutive_pos(min_row, min_col, max_row, max_col, start_pos):
        x, y = start_pos[0], start_pos[1]
        k = y - min_col
        return (x, y), (min_row + k, max_col), (max_row, max_col - k), (max_row - k, min_col)

    for i in range(n // 2):
        l = n - 2 * i
        min_row, min_col, max_row, max_col = i, i, i + l - 1, i + l - 1
        for k in range(l - 1):
            swap_four(matrix, *get_consecutive_pos(min_row, min_col, max_row, max_col, (i, i + k)))


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    print_matrix(matrix)
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    print_matrix(matrix)
    matrix = [[1]]
    rotate(matrix)
    print_matrix(matrix)
    matrix = [[1, 2], [3, 4]]
    rotate(matrix)
    print_matrix(matrix)
