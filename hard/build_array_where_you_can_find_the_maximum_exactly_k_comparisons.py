import unittest


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.num_of_arrays = Solution().numOfArrays

    def test_1(self):
        n, m, k = 2, 3, 1
        self.assertEqual(6, self.num_of_arrays(n, m, k))

    def test_2(self):
        n, m, k = 5, 2, 3
        self.assertEqual(0, self.num_of_arrays(n, m, k))

    def test_3(self):
        n, m, k = 9, 1, 1
        self.assertEqual(1, self.num_of_arrays(n, m, k))
