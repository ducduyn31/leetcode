import unittest
from collections import Counter, defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        new_s = []
        count_s = []

        for i in range(len(s)):
            if not new_s or new_s[-1] != s[i]:
                new_s.append(s[i])
                count_s.append(1)
            else:
                count_s[-1] += 1

        longest_sub_str = 0
        current_chars = set()
        left = right = 0

        while right < len(new_s):
            if len(current_chars) <= 2 or new_s[right] in current_chars:
                current_chars.add(new_s[right])
                right += 1
                current_len = count_s[right] if len(current_chars) == 1 else sum(count_s[left: right])
                longest_sub_str = max(longest_sub_str, current_len)
                continue

            while len(current_chars) > 1:
                left += 1


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.length_of_longest_substring_two_distinct = Solution().lengthOfLongestSubstringTwoDistinct

    def test_1(self):
        s = "eceba"
        self.assertEqual(3, self.length_of_longest_substring_two_distinct(s))

    def test_2(self):
        s = "ccaabbb"
        self.assertEqual(5, self.length_of_longest_substring_two_distinct(s))

    def test_3(self):
        s = "abc"
        self.assertEqual(2, self.length_of_longest_substring_two_distinct(s))

    def test_4(self):
        s = "a"
        self.assertEqual(1, self.length_of_longest_substring_two_distinct(s))
