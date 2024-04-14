import unittest
from collections import Counter, deque, defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        counter = defaultdict(int)
        window = deque()
        max_sum = 0

        current = 0
        for i in nums:
            if len(window) == k:
                j = window.popleft()
                current -= j
                if counter[j] == 1:
                    del counter[j]
                else:
                    counter[j] -= 1

            window.append(i)
            current += i
            counter[i] += 1

            if len(counter) >= m and len(window) == k:
                max_sum = max(max_sum, current)

        return max_sum


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.max_sum = Solution().maxSum

    def test_max_sum_should_return_18(self):
        self.assertEqual(18, self.max_sum([2, 6, 7, 3, 1, 7], 3, 4))

    def test_max_sum_should_return_23(self):
        self.assertEqual(23, self.max_sum([5, 9, 9, 2, 4, 5, 4], 1, 3))

    def test_max_sum_should_return_0(self):
        self.assertEqual(0, self.max_sum([1, 2, 1, 2, 1, 2, 1], 3, 3))

    def test_max_sum_should_return_3(self):
        self.assertEqual(3, self.max_sum([1, 2, 2], 2, 2))
