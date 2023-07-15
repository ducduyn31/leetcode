import unittest
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        result = []
        for n_pairs in range(n):
            left = self.generateParenthesis(n_pairs)
            right = self.generateParenthesis(n - n_pairs - 1)

            for left_str in left:
                for right_str in right:
                    result.append("(" + left_str + ")" + right_str)

        return result


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.generateParenthesis = Solution().generateParenthesis

    def test_generateParenthesis_should_return_1_empty_str_element(self):
        self.assertCountEqual([""], self.generateParenthesis(0))

    def test_generateParenthesis_should_return_1_element(self):
        self.assertCountEqual(["()"], self.generateParenthesis(1))

    def test_generateParenthesis_should_return_2_element(self):
        self.assertCountEqual(["()()", "(())"], self.generateParenthesis(2))

    def test_generateParenthesis_should_return_5_element(self):
        self.assertCountEqual(["(()())", "((()))", "(())()", "()()()", "()(())"], self.generateParenthesis(3))
