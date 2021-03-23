from typing import List


def moveZeroes(nums: List[int]) -> None:
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)


if __name__ == '__main__':
    nums = [0,1,0,3,12]

    moveZeroes(nums)

    print(nums)
