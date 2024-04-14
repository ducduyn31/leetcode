import unittest
from typing import List


class Solution:
    def processExecution(self, power: List[int], minPower: [int], maxPower: [int]) -> List[int]:
        power.sort()

        consumption = []
        process_count = []

        rng = []

        for i in range(len(minPower)):
            rng.append(minPower[i])
            rng.append(maxPower[i] + 1)

        rng.sort()
        current_power_idx = 0

        for i in range(len(rng) - 1):
            start = rng[i]
            end = rng[i + 1]

            current_process_count = 0
            current_consumption = 0

            while current_power_idx < len(power) and start <= power[current_power_idx] < end:
                current_consumption += power[current_power_idx]
                current_process_count += 1
                current_power_idx += 1

            consumption.append(current_consumption)
            process_count.append(current_process_count)

        result = [[0, 0] for _ in range(len(minPower))]

        for i in range(len(rng) - 1):
            start = rng[i]
            end = rng[i + 1]

            for j in range(len(minPower)):
                if minPower[j] <= start < end <= maxPower[j] + 1:
                    result[j][0] += process_count[i]
                    result[j][1] += consumption[i]

        return result


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.process_execution = Solution().processExecution

    def test_1(self):
        power = [7, 6, 8, 10]
        minPower = [6, 3, 4]
        maxPower = [10, 7, 9]

        self.assertEqual([[4, 31], [2, 13], [3, 21]], self.process_execution(power, minPower, maxPower))

    def test_2(self):
        power = [25, 56, 38, 31, 100]
        minPower = [20, 30, 40, 60]
        maxPower = [30, 40, 60, 120]

        self.assertEqual([[1, 25], [2, 69], [1, 56], [1, 100]], self.process_execution(power, minPower, maxPower))
