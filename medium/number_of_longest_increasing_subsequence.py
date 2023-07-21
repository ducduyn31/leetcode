import unittest
from bisect import bisect_left
from collections import Counter
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis, lis_endings = [], []

        for i, num in enumerate(nums):
            lis_len = bisect_left(lis, num)

            if lis_len == len(lis):
                lis.append(num)
                lis_endings.append([i])
            else:
                lis[lis_len] = num
                lis_endings[lis_len].append(i)

        def count_sequence(seq_len):
            if seq_len == 1:
                return [(i, 1) for i in lis_endings[seq_len - 1]]

            prev, res = count_sequence(seq_len - 1), []

            for i in lis_endings[seq_len - 1]:
                current_count = 0
                for j, prev_c in prev:
                    if j >= i:
                        break
                    if nums[j] < nums[i]:
                        current_count += prev_c
                res.append((i, current_count))

            return res

        return sum(c for _, c in count_sequence(len(lis)))


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.find_number_of_lis = Solution().findNumberOfLIS

    def test_find_number_of_lis_should_return_2_given_5_elements(self):
        self.assertEqual(2, self.find_number_of_lis([1, 3, 5, 4, 7]))

    def test_find_number_of_lis_should_return_5_given_5_elements(self):
        self.assertEqual(5, self.find_number_of_lis([2, 2, 2, 2, 2]))

    def test_find_number_of_lis_should_return_1_given_10_elements(self):
        self.assertEqual(1, self.find_number_of_lis([1, 10, 2, 9, 3, 8, 4, 7, 5, 6]))

    def test_find_number_of_lis_should_return_3_given_8_elements(self):
        self.assertEqual(3, self.find_number_of_lis([1, 2, 4, 3, 5, 4, 7, 2]))

    def test_find_number_of_lis_should_return_27_given_9_elements(self):
        self.assertEqual(27, self.find_number_of_lis([1, 1, 1, 2, 2, 2, 3, 3, 3]))
