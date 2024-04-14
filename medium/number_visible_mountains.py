import unittest
from typing import List


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        mountains = map(lambda peak: (peak[0] - peak[1], peak[0] + peak[1]), peaks)
        mountains = sorted(mountains, key=lambda peak: (peak[0], -peak[1]))
        visible_mountains = 0

        while len(mountains) > 0:
            (left, right) = mountains.pop(0)
            overlapped = False

            while len(mountains) > 0:
                (this_left, this_right) = mountains[0]
                if this_left > left and this_right > right:
                    break
                mountains.pop(0)
                if overlapped:
                    continue
                elif this_left == left and right == this_right:
                    overlapped = True

            visible_mountains += 0 if overlapped else 1

        return visible_mountains


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.visibleMountains = Solution().visibleMountains

    def test_visible_mountains_should_return_0_when_given_peaks_is_1_3_1_3(self):
        self.assertEqual(0, self.visibleMountains([[1, 3], [1, 3]]))

    def test_visible_mountains_should_return_0_when_given_peaks_are_multiple_1_3(self):
        self.assertEqual(0, self.visibleMountains([[1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3], [1, 3]]))

    def test_visible_mountains_should_return_1_when_given_peaks_is_1_1(self):
        self.assertEqual(1, self.visibleMountains([[1, 1]]))

    def test_visible_mountains_should_return_1_when_given_peaks_is_1_2_1(self):
        self.assertEqual(1, self.visibleMountains([[1, 2], [1, 1]]))

    def test_visible_mountains_should_return_1_when_given_peaks_is_1_2_2_1(self):
        self.assertEqual(1, self.visibleMountains([[1, 2], [2, 1]]))

    def test_visible_mountains_should_return_2_when_given_peaks_is_2_2_6_3_5_4(self):
        self.assertEqual(2, self.visibleMountains([[2, 2], [6, 3], [5, 4]]))
