import unittest
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        i = j = 0
        put_back = False

        while i < len(deck):
            if j >= len(deck):
                j = 0
                continue
            if result[j] > 0:
                j += 1
                continue
            if put_back:
                j += 1
                put_back = False
                continue

            result[j] = deck[i]
            put_back = True
            i += 1

        return result


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.deck_revealed_increasing = Solution().deckRevealedIncreasing

    def test_1(self):
        decks = [17, 13, 11, 2, 3, 5, 7]
        self.assertEqual(self.deck_revealed_increasing(decks), [2, 13, 3, 11, 5, 17, 7])

    def test_2(self):
        decks = [1, 1000]
        self.assertEqual(self.deck_revealed_increasing(decks), [1, 1000])
