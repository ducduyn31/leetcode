from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    first_id, second_id = 1, len(numbers)

    while first_id < second_id:
        temp_sum = numbers[first_id - 1] + numbers[second_id - 1]

        if temp_sum > target:
            second_id -= 1
        elif temp_sum < target:
            first_id += 1
        else:
            break

    return [first_id, second_id]


if __name__ == '__main__':
    assert twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    assert twoSum([5, 25, 75], 100) == [2, 3]
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert twoSum([2, 3, 4], 6) == [1, 3]
    assert twoSum([-1, 0], -1) == [1, 2]
