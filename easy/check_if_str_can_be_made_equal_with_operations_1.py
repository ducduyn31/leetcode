import unittest
from collections import Counter, defaultdict


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
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
        self.can_be_equal = Solution().canBeEqual

    def test_can_be_equal_should_return_true_given_abcd_cdab(self):
        self.assertTrue(self.can_be_equal('abcd', 'cdab'))

    def test_can_be_equal_should_return_false_given_abcd_dacb(self):
        self.assertFalse(self.can_be_equal('abcd', 'dacb'))

    def test_can_be_equal_should_return_false_given_jjgg_jgjg(self):
        self.assertFalse(self.can_be_equal('jjgg', 'gjgj'))

    def test_can_be_equal_should_return_true_given_riti_riti(self):
        self.assertTrue(self.can_be_equal('riti', 'riti'))
