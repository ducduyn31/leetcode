import math
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    result = []

    def find_next_smaller(sorted_list: List[int], point: int) -> int:
        def next_left(n: int) -> int:
            if n == 0:
                return n
            if sorted_list[n] == sorted_list[n - 1]:
                return next_left(n - 1)
            return n - 1

        def next_right(n: int) -> int:
            if n == len(sorted_list) - 1:
                return n
            if sorted_list[n] == sorted_list[n + 1]:
                return next_right(n + 1)
            return n + 1

        l = next_left(point)
        if abs(sorted_list[l]) < abs(sorted_list[point]):
            return l

        r = next_right(point)
        if abs(sorted_list[r]) < abs(sorted_list[point]):
            return r

        return point

    def find_min_id_by_slope(sorted_list: List[int], start_id: int, end_id: int) -> int:
        if start_id >= end_id:
            return start_id

        mid = (start_id + end_id) // 2
        next_smallest = find_next_smaller(sorted_list, mid)

        if next_smallest == mid:
            return mid

        if next_smallest < mid:
            return find_min_id_by_slope(sorted_list, start_id, next_smallest)

        return find_min_id_by_slope(sorted_list, next_smallest, end_id)

    min_id = find_min_id_by_slope(nums, 0, len(nums) - 1)
    result.append(nums[min_id] ** 2)
    left, right = min_id - 1, min_id + 1

    while len(result) < len(nums):
        if left < 0:
            result.append(nums[right] ** 2)
            right += 1
        elif right > len(nums) - 1:
            result.append(nums[left] ** 2)
            left -= 1
        elif abs(nums[right]) > abs(nums[left]):
            result.append(nums[left] ** 2)
        else:
            result.append(nums[right] ** 2)
            right += 1

    return result


if __name__ == '__main__':
    assert sortedSquares([-10, -3, -2, -2, -2, 1, 3, 3, 4, 8]) == [1, 4, 4, 4, 9, 9, 9, 16, 64, 100]
    assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
