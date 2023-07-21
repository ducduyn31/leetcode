import unittest
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        after_collision = []

        for asteroid in asteroids:
            while after_collision and asteroid < 0 < after_collision[-1]:
                if after_collision[-1] < -asteroid:
                    after_collision.pop()
                    continue
                elif after_collision[-1] == -asteroid:
                    after_collision.pop()
                break
            else:
                after_collision.append(asteroid)

        return after_collision


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.asteroid_collision = Solution().asteroidCollision

    def test_asteroid_collision_should_return_5_10_given_5_10_minus_5(self):
        self.assertEqual([5, 10], self.asteroid_collision([5, 10, -5]))

    def test_asteroid_collision_should_return_empty_given_8_minus_8(self):
        self.assertEqual([], self.asteroid_collision([8, -8]))

    def test_asteroid_collision_should_return_10_given_10_2_minus_5(self):
        self.assertEqual([10], self.asteroid_collision([10, 2, -5]))

    def test_asteroid_collision_should_return_minus_10_minus_5_given_minus_10_minus_5(self):
        self.assertEqual([-10, -5], self.asteroid_collision([-10, -5]))

    def test_asteroid_collision_should_return_correctly_given_asteroids(self):
        self.assertEqual([-10, -9], self.asteroid_collision([-10, 7, -9]))
