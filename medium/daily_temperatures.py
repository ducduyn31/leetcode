import unittest
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while temp_stack and temperatures[temp_stack[-1]] < temp:
                last = temp_stack.pop()
                result[last] = i - last
            temp_stack.append(i)

        return result


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.daily_temperatures = Solution().dailyTemperatures

    def test_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        self.assertEqual(
            [1, 1, 4, 2, 1, 1, 0, 0],
            self.daily_temperatures(temperatures),
        )

    def test_2(self):
        temperatures = [30, 40, 50, 60]
        self.assertEqual(
            [1, 1, 1, 0],
            self.daily_temperatures(temperatures),
        )

    def test_3(self):
        temperatures = [30, 60, 90]
        self.assertEqual(
            [1, 1, 0],
            self.daily_temperatures(temperatures),
        )
