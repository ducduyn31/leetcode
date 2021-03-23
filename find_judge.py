from typing import List


def findJudge(N: int, trust: List[List[int]]) -> int:
    is_trusted = [0 for _ in range(N)]
    is_trusting = [0 for _ in range(N)]

    for el in trust:
        is_trusted[el[1] - 1] += 1
        is_trusting[el[0] - 1] += 1

    for i in range(N):
        if is_trusted[i] == N - 1 and is_trusting[i] == 0:
            return i + 1
    return -1


if __name__ == '__main__':
    print(findJudge(2, [[1, 2]]))
    print(findJudge(3, [[1, 3], [2, 3]]))
    print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
    print(findJudge(3, [[1, 2], [2, 3]]))
    print(findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
