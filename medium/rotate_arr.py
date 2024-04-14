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


def assert_rotate(nums: List[int], k: int, result: List[int]):
    rotate(nums, k)
    assert nums == result


if __name__ == '__main__':
    assert_rotate([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
    assert_rotate([-1, -100, 3, 99], 2, [3, 99, -1, -100])
    assert_rotate([-1, -100, 3, 99], 0, [-1, -100, 3, 99])
