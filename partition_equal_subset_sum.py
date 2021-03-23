from typing import List


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0 or len(nums) < 2:
        return False
    half = total // 2
    nums = sorted(nums, reverse=True)
    if nums[0] == half:
        return True

    for i in range(1, len(nums)):
        current_sum = nums[0]
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > half:
                current_sum -= nums[j]
            elif current_sum == half:
                return True

    return False


if __name__ == '__main__':
    print(canPartition([1, 1, 2, 5, 5, 5, 5]))
    print(canPartition([1, 2, 3, 4, 5, 6, 7]))
    print(canPartition([2, 13, 1]))
    print(canPartition([23, 13, 11, 7, 6, 5, 5]))
    print(canPartition([2, 2, 1, 1]))
    print(canPartition([1, 5, 11, 5]))
    print(canPartition([1, 2, 3, 5]))
