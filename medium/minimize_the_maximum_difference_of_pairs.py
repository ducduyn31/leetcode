import unittest
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        min_threshold, max_threshold = 0, nums[-1] - nums[0]

        def count_pairs(threshold: int):
            index, count = 0, 0

            while index < len(nums) - 1:

                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1

                index += 1

            return count

        while min_threshold < max_threshold:
            threshold = min_threshold + (max_threshold - min_threshold) // 2

            if count_pairs(threshold) >= p:
                max_threshold = threshold
            else:
                min_threshold = threshold + 1

        return min_threshold


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.minimize_max = Solution().minimizeMax

    def test_minimize_max_should_return_1_given_p_2(self):
        nums = [10, 1, 2, 7, 1, 3]
        p = 2
        self.assertEqual(1, self.minimize_max(nums, p))

    def test_minimize_max_should_return_0_given_p_1(self):
        nums = [4, 2, 1, 2]
        p = 1
        self.assertEqual(0, self.minimize_max(nums, p))

    def test_minimize_max_should_return_1_given_p_3(self):
        nums = [3, 4, 2, 3, 2, 1, 2]
        p = 3
        self.assertEqual(1, self.minimize_max(nums, p))
