from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    mid = (left + right) // 2
    while left < right:
        if mid % 2 == 0:
            if nums[mid] == nums[mid - 1]:
                right = mid - 2
            elif nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                return nums[mid]
        else:
            if nums[mid] == nums[mid + 1]:
                right = mid - 1
            elif nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                return nums[mid]
        mid = (left + right) // 2
    return nums[mid]


if __name__ == '__main__':
    print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
