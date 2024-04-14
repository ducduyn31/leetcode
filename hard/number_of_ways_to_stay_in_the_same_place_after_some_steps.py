import unittest


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        def dp(pos: int, remain_steps):
            if pos == 0 and remain_steps == 1:
                return 1



            return 1 + dp(pos + 1, remain_steps - 1)

        return dp(0, steps)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.num_ways = Solution().numWays

    def test_1(self):
        self.assertEqual(4, self.num_ways(3, 2))

    def test_2(self):
        self.assertEqual(2, self.num_ways(2, 4))

    def test_3(self):
        self.assertEqual(8, self.num_ways(4, 2))
