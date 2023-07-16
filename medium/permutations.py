import unittest
from collections import deque
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permutation(deque(nums), [-1 for _ in nums], 0, result)
        return result

    def permutation(self, selection: deque, current_permutation: List[int], count: int, result: List[List[int]]):
        if count == len(current_permutation):
            result.append(current_permutation.copy())
            return

        for _ in range(len(current_permutation) - count):
            num = selection.popleft()
            current_permutation[count] = num
            self.permutation(selection, current_permutation, count + 1, result)
            selection.append(num)


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.permute = Solution().permute

    def test_permute_should_return_6_elements(self):
        actual = self.permute([1, 2, 3])
        self.assertCountEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], actual)

    def test_permute_should_return_2_elements(self):
        actual = self.permute([0, 1])
        self.assertCountEqual([[0, 1], [1, 0]], actual)

    def test_permute_should_return_1_element(self):
        actual = self.permute([1])
        self.assertCountEqual([[1]], actual)
