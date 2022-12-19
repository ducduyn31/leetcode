from typing import List


# def pivotIndex(nums: List[int]) -> int:
#     for i in range(len(nums)):
#         if sum(nums[:i]) == sum(nums[i + 1:]):
#             return i
#
#     return -1

# def pivotIndex(nums: List[int]) -> int:
#     def running_sum(l: List[int]) -> List[int]:
#         result = l.copy()
#         for i in range(1, len(result)):
#             result[i] = result[i - 1] + result[i]
#         return result
#
#     left_wise = running_sum(nums)
#     right_wise = running_sum(nums[::-1])
#
#     for i in range(len(left_wise)):
#         if left_wise[i] == right_wise[-i - 1]:
#             return i
#
#     return -1

def pivotIndex(nums: List[int]) -> int:
    left, right = 0, sum(nums)

    for i, n in enumerate(nums):
        right -= n
        if left == right:
            return i
        left += n

    return -1


if __name__ == '__main__':
    assert pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert pivotIndex([1, 2, 3]) == -1
    assert pivotIndex([2, 1, -1]) == 0
