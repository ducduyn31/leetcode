from typing import List


def generate(numRows: int) -> List[List[int]]:
    ans = []

    for r in range(numRows):
        row = [None for _ in range(r + 1)]
        row[0], row[-1] = 1, 1
        for c in range(1, r):
            row[c] = ans[-1][c-1] + ans[-1][c]
        ans.append(row)

    return ans


if __name__ == '__main__':
    print(generate(5))
