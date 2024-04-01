import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip()) - s.rstrip().rfind(" ") - 1


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.length_of_last_word = Solution().lengthOfLastWord

    def test_1(self):
        s = "Hello World"
        self.assertEqual(5, self.length_of_last_word(s))

    def test_2(self):
        s = "   fly me   to   the moon  "
        self.assertEqual(4, self.length_of_last_word(s))

    def test_3(self):
        s = "luffy is still joyboy"
        self.assertEqual(6, self.length_of_last_word(s))

    def test_4(self):
        s = " "
        self.assertEqual(0, self.length_of_last_word(s))
