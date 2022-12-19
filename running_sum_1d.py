from typing import List


# def runningSum(nums: List[int]) -> List[int]:
#     return [sum(nums[:i + 1]) for i in range(len(nums))]

def runningSum(nums: List[int]) -> List[int]:
    last_value = nums[0]
    result = [nums[0]] * len(nums)

    for i in range(1, len(nums)):
        result[i] = last_value + nums[i]
        last_value += nums[i]

    return result


if __name__ == '__main__':
    assert runningSum([1]) == [1]
    assert runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert runningSum([1, 2, -3, 4]) == [1, 3, 0, 4]
    assert runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
