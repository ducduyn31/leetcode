import unittest
from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = sandwiches[::-1]
        students = deque(students)

        while sandwiches:
            if students[0] == sandwiches[-1]:
                students.popleft()
                sandwiches.pop()
            else:
                count = len(students)

                while count > 0 and students[0] != sandwiches[-1]:
                    students.append(students.popleft())
                    count -= 1

                if count == 0:
                    break

        return len(students)


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.count_students = Solution().countStudents

    def test_1(self):
        students = [1, 1, 0, 0]
        sandwiches = [0, 1, 0, 1]
        self.assertEqual(0, self.count_students(students, sandwiches))

    def test_2(self):
        students = [1, 1, 1, 0, 0, 1]
        sandwiches = [1, 0, 0, 0, 1, 1]
        self.assertEqual(3, self.count_students(students, sandwiches))
