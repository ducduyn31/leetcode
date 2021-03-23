from typing import List


def rob(nums: List[int]) -> int:
    dp = [0, 0]

    for i in range(len(nums)):
        dp.append(max(dp[-1], dp[-2] + nums[i]))

    return dp[-1]


if __name__ == '__main__':
    print(rob([2, 1, 1, 2]))
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
