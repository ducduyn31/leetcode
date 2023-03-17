from typing import List


def findMaxLength2(nums: List[int]) -> int:
    max_len = 0

    miss_k_zeros = {0: -1}
    k = 0

    for i, n in enumerate(nums):
        if i == 0:
            k = -1 if n == 0 else 1
            miss_k_zeros[k] = 0
        else:
            next_inc = -1 if n == 0 else 1
            if k + next_inc not in miss_k_zeros:
                miss_k_zeros[k + next_inc] = i
            sub_arr_len = i - miss_k_zeros[k + next_inc]
            max_len = max(max_len, sub_arr_len)
            k += next_inc

    return max_len


def findMaxLength(nums: List[int]) -> int:
    nums = list(map(lambda x: -1 if x == 0 else 1, nums))

    hash_map = {}
    current_sum = 0
    max_len = 0

    for i, n in enumerate(nums):
        current_sum += n

        if current_sum == 0:
            max_len = i + 1

        if current_sum in hash_map:
            if max_len < i - hash_map[current_sum]:
                max_len = i - hash_map[current_sum]
        else:
            hash_map[current_sum] = i
    return max_len


if __name__ == '__main__':
    print(findMaxLength([0, 1]))
    print(findMaxLength([0, 1, 0]))
    print(findMaxLength([1, 0, 1, 1, 1, 0, 0]))
    print(findMaxLength([1, 1, 1, 1]))
    print(findMaxLength([0, 0, 1, 1, 0]))
    print(findMaxLength([0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]))
    print(findMaxLength([0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0]))
    print(findMaxLength([0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0]))
    print(findMaxLength([1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0]))
