from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    max_square = [0] * n
    d = 0
    end = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                temp = max_square[j]
                max_square[j] = min(max_square[j - 1], max_square[j], end) + 1

                if j == n - 1:
                    end = 0
                else:
                    end = temp

                if max_square[j] > d:
                    d = max_square[j]
            else:
                max_square[j] = 0

    return d * d


if __name__ == '__main__':
    print(maximalSquare(
        [["1"], ["0"], ["1"], ["1"], ["1"], ["1"], ["0"]]))
    print(maximalSquare(
        []))
    print(maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
    print(maximalSquare(
        [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]]))
