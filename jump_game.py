from typing import List


def canJump(nums: List[int]) -> bool:
    N = len(nums)
    start = N - 1

    for loc in range(N - 1, -1, -1):
        if loc + nums[loc] >= start:
            start = loc

    return start == 0


if __name__ == '__main__':
    print(canJump([2, 0]))
    print(canJump([0]))
    print(canJump([2, 3, 1, 1, 4]))
    print(canJump([3, 2, 1, 0, 4]))
