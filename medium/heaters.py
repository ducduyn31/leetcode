import bisect
import unittest
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        min_rad = 0
        i = 0

        while i < len(houses):
            closest_heater_id = self.find_closest(heaters, houses[i])
            rad = abs(houses[i] - heaters[closest_heater_id])
            min_rad = max(min_rad, rad)

            i = max(self.find_closest(houses, heaters[closest_heater_id] + rad), i + 1)

        return min_rad

    def find_closest(self, arr: List[int], target: int) -> int:
        closest_left_id = bisect.bisect_left(arr, target)
        if closest_left_id == len(arr):
            return len(arr) - 1
        elif arr[closest_left_id] == target:
            return closest_left_id
        closest_right_id = bisect.bisect_right(arr, target, closest_left_id)
        distance_left = abs(arr[closest_left_id - 1] - target)
        distance_right = abs(arr[closest_right_id] - target)
        if distance_right > distance_left:
            return closest_left_id - 1
        return closest_right_id


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.find_radius = Solution().findRadius

    def test_1(self):
        houses = [1, 2, 3]
        heaters = [2]
        self.assertEqual(1, self.find_radius(houses, heaters))

    def test_2(self):
        houses = [1, 2, 3, 4]
        heaters = [1, 4]
        self.assertEqual(1, self.find_radius(houses, heaters))

    def test_3(self):
        houses = [1, 5]
        heaters = [2]
        self.assertEqual(3, self.find_radius(houses, heaters))

    def test_4(self):
        houses = [1, 5]
        heaters = [10]
        self.assertEqual(9, self.find_radius(houses, heaters))

    def test_5(self):
        houses = [5, 6, 10, 12]
        heaters = [1, 8, 13]
        self.assertEqual(3, self.find_radius(houses, heaters))

    def test_6(self):
        houses = [1, 2, 3]
        heaters = [1, 2, 3]
        self.assertEqual(0, self.find_radius(houses, heaters))
