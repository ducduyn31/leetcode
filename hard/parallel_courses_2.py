import unittest
from collections import defaultdict
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        indegree, children = [0] * n, defaultdict(list)

        for start, end in relations:
            indegree[end - 1] += 1
            children[start - 1].append(end - 1)

        stack = []

        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)

        sem_cnt = 0

        while stack:
            sem_cnt += 1
            cnt = 0
            next_sems = []
            while stack:
                if cnt == k:
                    break
                current = stack.pop()
                n -= 1
                cnt += 1

                for child in children[current]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        next_sems.append(child)

            if n == 0:
                return sem_cnt
            stack.extend(next_sems)

        return -1


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.min_number_of_semesters = Solution().minNumberOfSemesters

    def test_1(self):
        n = 4
        relations = [[2, 1], [3, 1], [1, 4]]
        k = 2

        self.assertEqual(3, self.min_number_of_semesters(n, relations, k))

    def test_2(self):
        n = 5
        relations = [[2, 1], [3, 1], [4, 1], [1, 5]]
        k = 2

        self.assertEqual(4, self.min_number_of_semesters(n, relations, k))

    def test_3(self):
        n = 11
        relations = []
        k = 2

        self.assertEqual(6, self.min_number_of_semesters(n, relations, k))

    def test_4(self):
        n = 13
        relations = [
            [12, 8],
            [2, 4],
            [3, 7],
            [6, 8],
            [11, 8],
            [9, 4],
            [9, 7],
            [12, 4],
            [11, 4],
            [6, 4],
            [1, 4],
            [10, 7],
            [10, 4],
            [1, 7],
            [1, 8],
            [2, 7],
            [8, 4],
            [10, 8],
            [12, 7],
            [5, 4],
            [3, 4],
            [11, 7],
            [7, 4],
            [13, 4],
            [9, 8],
            [13, 8],
        ]
        k = 9

        self.assertEqual(3, self.min_number_of_semesters(n, relations, k))
