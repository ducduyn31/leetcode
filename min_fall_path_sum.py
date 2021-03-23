from typing import List


def minFallingPathSum(A: List[List[int]]) -> int:
    if len(A) == 1:
        return A[0][0]

    paths = A[:][:]

    for row in range(1, len(A)):
        for col in range(len(A)):
            if col == 0:
                paths[row][col] = min(paths[row - 1][0] + A[row][col], paths[row - 1][1] + A[row][col])
            elif col == len(A) - 1:
                paths[row][col] = min(paths[row - 1][col] + A[row][col], paths[row - 1][col - 1] + A[row][col])
            else:
                paths[row][col] = min(paths[row - 1][col - 1] + A[row][col], paths[row - 1][col] + A[row][col], paths[row - 1][col + 1] + A[row][col])

    return min(A[-1])


if __name__ == '__main__':
    print(minFallingPathSum([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]]))
