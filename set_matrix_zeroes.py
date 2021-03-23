from typing import List


def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)


def setZeroes(matrix: List[List[int]]) -> None:
    zero_rows, zero_columns = set(), set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_columns.add(col)

    for row in zero_rows:
        matrix[row] = [0] * len(matrix[0])
    for col in zero_columns:
        for row in range(len(matrix)):
            matrix[row][col] = 0


if __name__ == '__main__':
    mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(mat)
    print_matrix(mat)
    mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(mat)
    print_matrix(mat)
