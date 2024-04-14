import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        return x_str == x_str[::-1]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.is_palindrome = Solution().isPalindrome

    def test_1(self):
        self.assertTrue(self.is_palindrome(121))

    def test_2(self):
        self.assertFalse(self.is_palindrome(-121))
