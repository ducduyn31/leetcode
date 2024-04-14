import unittest
from collections import defaultdict


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd = defaultdict(int)
        even = defaultdict(int)

        for i in range(len(s1)):
            if i % 2 == 0:
                even[s1[i]] += 1
            else:
                odd[s1[i]] += 1

        for j in range(len(s2)):
            if j % 2 == 0:
                if s2[j] in even and even[s2[j]] > 0:
                    even[s2[j]] -= 1
                else:
                    return False
            else:
                if s2[j] in odd and odd[s2[j]] > 0:
                    odd[s2[j]] -= 1
                else:
                    return False

        return True


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.check_strings = Solution().checkStrings

    def test_check_strs_should_return_true_given_abcdba_cabdab(self):
        self.assertTrue(self.check_strings('abcdba', 'cabdab'))

    def test_check_strs_should_return_false_given_abe_bea(self):
        self.assertFalse(self.check_strings('abe', 'bea'))
