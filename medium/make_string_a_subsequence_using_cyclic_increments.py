import unittest


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = j = 0

        def is_cyclic_equal(char1: str, char2: str) -> bool:
            return char1 == char2 or (ord(char2) - ord(char1)) % 26 == 1

        while i < len(str1) and j < len(str2):
            if is_cyclic_equal(str1[i], str2[j]):
                j += 1
            i += 1

        return j == len(str2)


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.can_make_subsequence = Solution().canMakeSubsequence

    def test_1(self) -> None:
        self.assertTrue(self.can_make_subsequence('abc', 'ad'))

    def test_2(self) -> None:
        self.assertTrue(self.can_make_subsequence('zc', 'ad'))

    def test_3(self) -> None:
        self.assertFalse(self.can_make_subsequence('ab', 'd'))
