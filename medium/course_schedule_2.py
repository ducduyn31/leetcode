import unittest
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [0] * numCourses
        requirements = defaultdict(list)

        for course, requirement in prerequisites:
            courses[course] += 1
            requirements[requirement].append(course)

        Q = deque()
        result = []

        for course in range(numCourses):
            if courses[course] == 0:
                Q.append(course)

        count = 0

        while Q:
            current = Q.popleft()
            result.append(current)
            count += 1

            for prerequisite in requirements[current]:
                courses[prerequisite] -= 1
                if courses[prerequisite] == 0:
                    Q.append(prerequisite)

        return result if count == numCourses else []


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.findOrder = Solution().findOrder

    def test_find_order_given_1_0_should_return_0_1(self):
        self.assertEqual([0, 1], self.findOrder(2, [[1, 0]]))

    def test_find_order_given_1_0_2_0_3_1_3_2_should_return_0_1_2_3(self):
        self.assertEqual([0, 1, 2, 3], self.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    def test_find_order_given_empty_should_return_0(self):
        self.assertEqual([0], self.findOrder(1, []))

    def test_find_order_given_1_0_1_2_0_1_should_return_empty(self):
        self.assertEqual([], self.findOrder(3, [[1, 0], [1, 2], [0, 1]]))
