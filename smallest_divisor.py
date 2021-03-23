from math import ceil
from typing import List


def smallestDivisor(nums: List[int], threshold: int) -> int:
    def sum_div_ceil(l: List[int], divisor: int) -> int:
        return sum(map(lambda x: ceil(x / divisor), l))

    low = 1
    high = max(nums)
    last = 0

    while low <= high:
        mid = (high + low) // 2

        if sum_div_ceil(nums, mid) <= threshold:
            last = mid
            high = mid - 1
        else:
            low = mid + 1
    return last

if __name__ == '__main__':
    print(smallestDivisor([1, 2, 5, 9], 6))
    print(smallestDivisor([2, 3, 5, 7, 11], 11))
    print(smallestDivisor([19], 5))
