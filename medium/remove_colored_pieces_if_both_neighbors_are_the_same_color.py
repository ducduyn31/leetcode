import unittest


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False

        chances_A = chances_B = 0

        a_counter = 0
        b_counter = 0

        for c in colors:
            if c == 'A':
                a_counter += 1
                b_counter = 0
                if a_counter >= 3:
                    chances_A += 1
            else:
                b_counter += 1
                a_counter = 0
                if b_counter >= 3:
                    chances_B += 1

        return chances_A > chances_B


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.winner_of_game = Solution().winnerOfGame

    def test_1(self):
        self.assertTrue(self.winner_of_game('AAABABB'))

    def test_2(self):
        self.assertFalse(self.winner_of_game('AA'))

    def test_3(self):
        self.assertFalse(self.winner_of_game('ABBBBBBBAAA'))
