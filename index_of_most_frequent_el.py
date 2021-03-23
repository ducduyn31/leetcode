import random
from collections import defaultdict
from typing import List


def findRandomIndexOfMax(arr: List[int]) -> int:
    F = defaultdict(int)

    for i, n in enumerate(arr):
        F[n] += 1

    l = sorted(F.items(), key=lambda x: x[1], reverse=True)
    top, frequency = l[0]
    tops = []

    for t, f in l:
        if f != frequency:
            break
        tops.append(t)

    ids = []
    for i, n in enumerate(arr):
        if n in tops:
            ids.append(i)

    return random.choice(ids)


if __name__ == '__main__':
    print(findRandomIndexOfMax([-1, 4, 9, 7, 7, 2, 7, 3, 0, 9, 6, 5, 7, 8, 9]))
