from collections import defaultdict
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    current_sum = 0
    previous_sum = {}
    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum == k:
            count += 1

        if (current_sum - k) in previous_sum:
            count += previous_sum[current_sum - k]

        previous_sum[current_sum] = previous_sum.get(current_sum, 0) + 1

    return count


if __name__ == '__main__':
    # print(subarraySum([1, 1, 1], 2))
    # print(subarraySum([-1, -1, 1], 0))
    # print(subarraySum([1], 0))
    # print(subarraySum([1, 2, 3], 3))
    print(subarraySum([1, 1, 1, -2, 3], 2))
