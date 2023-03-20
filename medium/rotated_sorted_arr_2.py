from typing import List


def search(nums: List[int], target: int) -> bool:
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True

        if nums[left] < nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[left] == nums[mid]:
            left += 1
        elif nums[mid] <= target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == '__main__':
    print(search([3, 1], 1))
    print(search([3, 5, 1], 3))
    print(search([2, 5, 6, 0, 0, 1, 2], 3))
    print(search([2, 5, 6, 0, 0, 1, 2], 0))
