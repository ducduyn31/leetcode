import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) - 1 == 0:
            return 0

        dp = [1]
        last_reach = 0

        for i in range(len(nums)):
            if last_reach >= len(nums) - 1:
                break
            for j in range(last_reach, min(len(nums) - 1, i + nums[i])):
                if i == 0:
                    dp.append(1)
                else:
                    dp.append(dp[i] + 1)

            last_reach = min(max(last_reach, i + nums[i]), len(nums) - 1)

        return dp[-1]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.jump = Solution().jump

    def test_jump_should_return_2_given_5_elements(self):
        self.assertEqual(2, self.jump([2, 3, 1, 1, 4]))

    def test_jump_should_return_2_given_other_5_elements(self):
        self.assertEqual(2, self.jump([2, 3, 0, 1, 4]))

    def test_jump_should_return_0_given_other_1_element(self):
        self.assertEqual(0, self.jump([1]))

    def test_jump_should_return_3_given_other_4_elements(self):
        self.assertEqual(3, self.jump([1, 1, 1, 1]))
