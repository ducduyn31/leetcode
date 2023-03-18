from typing import List


def moveZeroes(nums: List[int]) -> None:
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)


def assert_move(nums: List[int], result: List[int]):
    moveZeroes(nums)
    assert nums == result


if __name__ == '__main__':
    assert_move([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
    assert_move([0], [0])
