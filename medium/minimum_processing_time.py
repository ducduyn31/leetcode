import unittest
from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)

        max_time = 0

        for i, t in enumerate(tasks):
            max_time = max(max_time, processorTime[i // 4] + t)

        return max_time


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.min_processing_time = Solution().minProcessingTime

    def test_1(self):
        processorTime = [8, 10]
        tasks = [2, 2, 3, 1, 8, 7, 4, 5]
        self.assertEqual(16, self.min_processing_time(processorTime, tasks))

    def test_2(self):
        processorTime = [10, 20]
        tasks = [2, 3, 1, 2, 5, 8, 4, 3]
        self.assertEqual(23, self.min_processing_time(processorTime, tasks))
