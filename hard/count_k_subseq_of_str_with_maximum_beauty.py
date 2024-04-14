import math
import unittest
from collections import Counter


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        counter = Counter(s)
        if len(counter) < k:
            return 0

        characters, freq = list(zip(*counter.most_common()))
        result = 1
        last_character_freq = freq[k - 1]
        should_combine_characters = list(freq).count(last_character_freq)
        remaining = 0

        for i in range(k):
            if freq[i] != last_character_freq:
                result *= freq[i]
            else:
                remaining += 1

        result *= math.comb(should_combine_characters, remaining)
        result *= last_character_freq ** remaining
        modulo = 1_000_000_007

        return result % modulo


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.count = Solution().countKSubsequencesWithMaxBeauty

    def test_count_should_return_4(self):
        self.assertEqual(4, self.count('bcca', 2))

    def test_count_should_return_2(self):
        self.assertEqual(2, self.count('abbcd', 4))

    def test_count_should_return_0(self):
        self.assertEqual(0, self.count('dd', 2))

    def test_count_should_return_106920(self):
        self.assertEqual(106920, self.count('hdzwklstebqbfvuxbryrpxurlxh', 10))
