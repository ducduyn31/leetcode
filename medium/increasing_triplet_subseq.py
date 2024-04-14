from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    first, second = float('inf'), float('inf')

    for n in nums:
        if n < first and n < second:
            first = n
        elif first < n < second:
            second = n
        elif first < second < n:
            return True

    return False


if __name__ == '__main__':
    print(increasingTriplet([1, 2, 3, 4, 5]))
    print(increasingTriplet([5, 4, 3, 2, 1]))
