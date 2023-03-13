from typing import List


def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    assert search([0], 0) == 0
    assert search([0], -2) == -1
    assert search([0, 2], 2) == 1
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 7, 9, 12], 9) == 5
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
