import unittest


class Solution:

    def calculate(self, s: str) -> int:
        s = f'({s})'

        def evaluate_operation(a, b, operator):
            if operator == '+':
                return a + b
            elif operator == '-':
                return a - b
            elif operator == '*':
                return a * b
            else:
                return int(a / b)

        def solve_expression(start_idx):
            S = []
            current_idx = start_idx

            current_number = 0
            operation = '+'

            while current_idx < len(s):
                if s[current_idx].isdigit():
                    current_number = current_number * 10 + int(s[current_idx])
                elif s[current_idx] in {'+', '-', '*', '/', ')'}:
                    if operation in {'+', '-'}:
                        S.append(evaluate_operation(0, current_number, operation))
                    else:
                        S.append(evaluate_operation(S.pop(), current_number, operation))

                    current_number = 0
                    if s[current_idx] != ')':
                        operation = s[current_idx]
                    else:
                        break
                elif s[current_idx] == '(':
                    current_number, current_idx = solve_expression(current_idx + 1)

                current_idx += 1

            return sum(S), current_idx

        return solve_expression(1)[0]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calculate = Solution().calculate

    def test_1(self):
        self.assertEqual(2, self.calculate("1+1"))

    def test_2(self):
        self.assertEqual(4, self.calculate("6-4/2"))

    def test_3(self):
        self.assertEqual(21, self.calculate("2*(5+5*2)/3+(6/2+8)"))
