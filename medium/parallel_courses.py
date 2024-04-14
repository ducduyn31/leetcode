import unittest
from collections import defaultdict
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        children = defaultdict(list)
        indegree = [0] * n

        for prev, next in relations:
            children[prev - 1].append(next - 1)
            indegree[next - 1] += 1

        current_courses = []

        for i in range(n):
            if indegree[i] == 0:
                current_courses.append(i)

        if not current_courses:
            return -1

        cnt = 0

        while current_courses:
            cnt += 1
            next_courses = []
            while current_courses:
                n -= 1
                current_course = current_courses.pop()
                for child in children[current_course]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        next_courses.append(child)

            current_courses = next_courses
            if n == 0:
                return cnt

        return -1


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.minimum_semesters = Solution().minimumSemesters

    def test_1(self):
        n = 3
        relations = [[1, 3], [2, 3]]

        self.assertEqual(2, self.minimum_semesters(n, relations))

    def test_2(self):
        n = 3
        relations = [[1, 2], [2, 3], [3, 1]]

        self.assertEqual(-1, self.minimum_semesters(n, relations))

    def test_3(self):
        n = 4
        relations = [[1, 2], [2, 3], [3, 4], [4, 2]]

        self.assertEqual(-1, self.minimum_semesters(n, relations))
