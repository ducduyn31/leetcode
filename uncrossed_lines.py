from typing import List


def maxUncrossedLines(A: List[int], B: List[int]) -> int:
    m = len(A)
    n = len(B)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            alpha = 1 if A[i] == B[j] else 0
            dp[i][j] = max(dp[i + 1][j], max(dp[i][j + 1], dp[i + 1][j + 1] + alpha))

    return dp[0][0]

if __name__ == '__main__':
    print(maxUncrossedLines([1, 4, 2], [1, 2, 4]))
    print(maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
    print(maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
