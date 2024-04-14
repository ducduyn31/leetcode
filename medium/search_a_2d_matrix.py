import unittest
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        H, W = len(matrix), len(matrix[0])
        N = H * W - 1

        def get_value(index):
            x = index % W
            y = index // W

            return matrix[y][x]

        left, right = 0, N

        if target == get_value(left) or target == get_value(right):
            return True

        while left <= right:
            mid = (left + right) // 2
            mid_val = get_value(mid)

            if mid_val == target:
                return True
            if mid_val > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.search_matrix = Solution().searchMatrix

    def test_search_matrix_should_return_true_given_target_3(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        self.assertTrue(self.search_matrix(matrix, target))

    def test_search_matrix_should_return_false_given_target_13(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(self.search_matrix(matrix, target))

    def test_search_matrix_should_return_true_given_target_2(self):
        matrix = [[1, 1], [2, 2]]
        target = 2
        self.assertTrue(self.search_matrix(matrix, target))

    def test_search_matrix_should_return_true_given_target_3_and_small_matrix(self):
        matrix = [[1], [3]]
        target = 3
        self.assertTrue(self.search_matrix(matrix, target))
