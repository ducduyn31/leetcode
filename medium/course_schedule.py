import unittest
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite_to_course_map = defaultdict(list)
        course_to_prerequisite_map = defaultdict(set)
        course_queue = []

        for [course_id, prerequisite_course_id] in prerequisites:
            prerequisite_to_course_map[prerequisite_course_id].append(course_id)
            course_to_prerequisite_map[course_id].add(prerequisite_course_id)

        for course_id in range(numCourses):
            if course_id not in course_to_prerequisite_map:
                course_queue.append(course_id)

        while len(course_queue) > 0:
            course_id = course_queue.pop(0)
            if course_id in prerequisite_to_course_map:
                depended_courses = prerequisite_to_course_map.pop(course_id)
                for c in depended_courses:
                    course_to_prerequisite_map[c].remove(course_id)
                    if len(course_to_prerequisite_map[c]) == 0:
                        del course_to_prerequisite_map[c]
                        course_queue.append(c)

        return len(prerequisite_to_course_map.keys()) == 0


class SolutionUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.canFinish = Solution().canFinish

    def test_canFinish_should_return_true_when_no_prerequisite(self) -> None:
        self.assertEqual(self.canFinish(2, []), True)

    def test_canFinish_should_return_true_when_no_prerequisite_loop(self) -> None:
        self.assertEqual(self.canFinish(2, [[1, 0]]), True)

    def test_canFinish_should_return_false_when_prerequisites_loop(self) -> None:
        self.assertEqual(self.canFinish(2, [[1, 0], [0, 1]]), False)

    def test_canFinish_should_return_true_when_no_prerequisite_loop_3(self) -> None:
        self.assertEqual(self.canFinish(3, [[1, 0], [0, 2], [2, 1]]), False)

    def test_canFinish_should_return_true_when_prerequisite_loop_3(self) -> None:
        self.assertEqual(self.canFinish(3, [[1, 0], [0, 2]]), True)
