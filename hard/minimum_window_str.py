import unittest
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        remaining = Counter(t)
        t_keys = set(remaining.keys())
        s_list = []

        for i, c in enumerate(s):
            if c in remaining:
                s_list.append((c, i))

        left, right = 0, 0
        start, end = 0, float("inf")

        while right < len(s_list):
            c_right, pos_right = s_list[right]
            remaining.subtract(c_right)

            if remaining[c_right] <= 0 and c_right in t_keys:
                t_keys.remove(c_right)

            while left <= right and not t_keys:
                c_left, pos_left = s_list[left]
                remaining.update(c_left)
                left += 1

                if remaining[c_left] > 0 and c_left not in t_keys:
                    t_keys.add(c_left)

                if pos_right - pos_left < end - start:
                    start = pos_left
                    end = pos_right

            right += 1

        return "" if end == float("inf") else s[start: end + 1]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.min_window = Solution().minWindow

    def test_1(self):
        self.assertEqual("BANC", self.min_window("ADOBECODEBANC", "ABC"))

    def test_2(self):
        self.assertEqual("a", self.min_window("a", "a"))

    def test_3(self):
        self.assertEqual("", self.min_window("a", "aa"))

    def test_4(self):
        self.assertEqual("ba", self.min_window("bba", "ba"))

    def test_5(self):
        self.assertEqual("baa", self.min_window("bbaac", "aba"))
