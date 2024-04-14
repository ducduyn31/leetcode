import unittest


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if row >= n or column >= n or row < 0 or column < 0:
            return 0.0

        if k == 0 and row < n and column < n:
            return 1.0

        visited = [[[-1.0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]

        def prob_for_step(step: int, r: int, c: int):
            if step == 0 and 0 <= r < n and 0 <= c < n:
                return 1.0
            elif step == 0:
                return 0.0

            if visited[step][r][c] >= 0:
                return visited[step][r][c]

            candidates = [
                (r - 2, c - 1), (r - 1, c - 2), (r + 1, c - 2), (r + 2, c - 1),
                (r + 2, c + 1), (r + 1, c + 2), (r - 1, c + 2), (r - 2, c + 1),
            ]

            visited[step][r][c] = 0
            for y, x in candidates:
                if 0 <= x < n and 0 <= y < n:
                    visited[step][r][c] += prob_for_step(step - 1, y, x)

            visited[step][r][c] /= 8

            return visited[step][r][c]

        return prob_for_step(k, row, column)


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.knight_probability = Solution().knightProbability

    def test_knight_probability_should_return_006250(self):
        self.assertEqual(0.0625, self.knight_probability(3, 2, 0, 0))

    def test_knight_probability_should_return_1(self):
        self.assertEqual(1.0, self.knight_probability(1, 0, 0, 0))

    def test_knight_probability_should_return_000019(self):
        self.assertEqual(0.00019, self.knight_probability(8, 30, 6, 4))
