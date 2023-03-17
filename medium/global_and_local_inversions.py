from typing import List


def isIdealPermutation(A: List[int]) -> bool:
    for i, n in enumerate(A):
        if abs(n - i) > 1:
            return False
    return True


if __name__ == '__main__':
    print(isIdealPermutation([1, 0, 2]))
    print(isIdealPermutation([1, 2, 0]))
