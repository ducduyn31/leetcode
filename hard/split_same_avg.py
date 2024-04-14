from typing import List


def splitArraySameAverage(A: List[int]) -> bool:
    if len(A) == 1:
        return False
    N = len(A)
    S = sum(A)
    A = [x * N - S for x in A]

    left = {A[0]}
    for i in range(1, N // 2):
        left |= {z + A[i] for z in left} | {A[i]}

    right = {A[-1]}
    for i in range(N // 2, N - 1):
        right |= {z + A[i] for z in right} | {A[i]}
    if 0 in right | left:
        return True
    left -= {sum(A[:N // 2])}
    return any(-a in left for a in right)


if __name__ == '__main__':
    print(splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))
    print(splitArraySameAverage([3, 1]))
    print(splitArraySameAverage([15, 2, 8, 2]))
    print(splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))
