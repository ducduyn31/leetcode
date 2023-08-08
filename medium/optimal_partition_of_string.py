import unittest


class Solution:
    def partitionString(self, s: str) -> int:
        last_seen = [-1] * 26
        substr_start = 0
        count = 1

        for i, c in enumerate(s):
            if last_seen[ord(c) - ord('a')] >= substr_start:
                count += 1
                substr_start = i

            last_seen[ord(c) - ord('a')] = i

        return count


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.partition_string = Solution().partitionString

    def test_partition_string_should_return_4_given_abacaba(self):
        self.assertEqual(4, self.partition_string('abacaba'))

    def test_partition_string_should_return_6_given_ssssss(self):
        self.assertEqual(6, self.partition_string('ssssss'))
