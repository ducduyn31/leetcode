from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] <= target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    print(search([0, 1, 2, 4, 5, 6, 7], 0))
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
    print(search([4, 5, 6, 7, 0, 1, 2], 3))
    print(search([1, 3], 0))
    print(search([3, 1], 0))
    print(search([3, 1], 3))
    print(search([3, 5, 1], 5))
    print(search([9, 0, 2, 7, 8], 3))
    print(search([], 3))
