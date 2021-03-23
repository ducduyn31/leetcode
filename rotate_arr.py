from typing import List


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n

    i = j = 0
    while i < n:
        current_id, last = j, nums[j]
        while True:
            current_id = (current_id + k) % n
            nums[current_id], last = last, nums[current_id]
            i += 1
            if current_id == j:
                break

        j += 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)
    nums = [-1, -100, 3, 99]
    rotate(nums, 2)
    print(nums)
    nums = [-1, -100, 3, 99]
    rotate(nums, 0)
    print(nums)
