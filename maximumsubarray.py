from typing import List


def maxSubArray(nums: List[int]) -> int:

    max_sum_subarr = nums[0]
    temp = 0

    for i, n in enumerate(nums):
        if n > temp + n:
            temp = n
        else:
            temp += n

        if temp > max_sum_subarr:
            max_sum_subarr = temp

    return max_sum_subarr


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
