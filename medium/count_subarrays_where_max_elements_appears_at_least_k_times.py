import unittest
from collections import Counter
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        current_count = Counter()
        max_number = 0
        count_subarr = 0
        left = right = 0

        while right < len(nums):
            current_count[nums[right]] += 1
            max_number = max(max_number, nums[right])

            if current_count[max_number] >= k:
                count_subarr += 1

                while current_count[max_number] > k:
                    current_count[nums[left]] -= 1
                    left += 1

                    if current_count[max_number] == 0:
                        max_number = max(nums[left:right + 1])

                    if current_count[max_number] >= k:
                        count_subarr += 1

            right += 1

        while left < right -1:
            current_count[nums[left]] -= 1
            left += 1

            if current_count[max_number] == 0:
                max_number = max(nums[left: right + 1])

            if current_count[max_number] >= k:
                count_subarr += 1

        return count_subarr


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.count_subarrays = Solution().countSubarrays

    def test_1(self):
        nums = [1, 3, 2, 3, 3]
        k = 2
        self.assertEqual(6, self.count_subarrays(nums, k))

    def test_2(self):
        nums = [1, 4, 2, 1]
        k = 3
        self.assertEqual(0, self.count_subarrays(nums, k))
