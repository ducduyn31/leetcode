import unittest
from collections import Counter
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.combination_to_target(candidates, target, 0, result, [])
        return result

    def combination_to_target(self, candidates: List[int], target: int, start: int,
                              result: List[List[int]], current_combination: List[int]):
        if target == 0:
            result.append(current_combination.copy())
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                current_combination.append(candidates[i])
                self.combination_to_target(candidates, target - candidates[i], i, result, current_combination)
                current_combination.pop()
            else:
                break


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.combination_sum = Solution().combinationSum

    def assertNestedCountEqual(self, expected: List[List], actual: List[List]):
        if len(expected) == len(actual) == 0:
            self.assertCountEqual(expected, actual)
        expected_with_counter = [Counter(el) for el in expected]
        actual_with_counter = [Counter(el) for el in actual]
        self.assertCountEqual(expected_with_counter, actual_with_counter)

    def test_combination_sum_should_return_2_elements_given_7(self):
        actual = self.combination_sum([2, 3, 6, 7], 7)
        self.assertNestedCountEqual([[2, 2, 3], [7]], actual)

    def test_combination_sum_should_return_3_elements_given_8(self):
        actual = self.combination_sum([2, 3, 5], 8)
        self.assertNestedCountEqual([[2, 2, 2, 2], [2, 3, 3], [3, 5]], actual)

    def test_combination_sum_should_return_0_element_given_1(self):
        actual = self.combination_sum([2], 1)
        self.assertNestedCountEqual([], actual)
