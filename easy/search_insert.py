from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid

    return mid + 1 if nums[mid] < target else mid


if __name__ == '__main__':
    assert searchInsert([1, 3, 5, 6], 5) == 2
    assert searchInsert([1, 3, 5, 6], 2) == 1
    assert searchInsert([1, 3, 5, 6], 7) == 4
    assert searchInsert([1, 3, 5, 6], 0) == 0
    assert searchInsert([1], 0) == 0
