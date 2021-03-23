from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


if __name__ == '__main__':
    print(missingNumber([3, 0, 1]))
    print(missingNumber([0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([0]))
