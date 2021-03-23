from typing import List


def countSquares(matrix: List[List[int]]) -> int:
    squares = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                squares[row + 1][col + 1] = min(squares[row][col], squares[row][col + 1], squares[row + 1][col]) + 1
    result = 0
    for r in squares:
        result += sum(r)

    return result


if __name__ == '__main__':
    print(countSquares([
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 1],
        [1, 1, 0]]))
    print(countSquares([
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [1, 0, 0, 1, 1]
    ]))
    print(countSquares([
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]))
    print(countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]))

    print(countSquares([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]))
