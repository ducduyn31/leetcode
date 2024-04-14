import unittest


class Solution:

    def solution(self, lamps):
        rng = []

        for i in range(len(lamps)):
            loc = lamps[i][0]
            rad = lamps[i][1]

            rng .append((loc - rad, 0))
            rng .append((loc + rad, 1))

        rng.sort()
        count = 0
        max_ilum = 0
        max_id = 0

        for i in range(len(rng)):
            if rng[i][1] == 0:
                count += 1
            else:
                count -= 1

            if count > max_ilum:
                max_ilum = count
                max_id = i
        return rng[max_id][0]





class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution().solution

    def test_1(self):
        lamps = [[-2, 3], [2, 3], [2, 1]]
        self.assertEqual(1, self.solution(lamps))
