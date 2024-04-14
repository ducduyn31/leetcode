import unittest
from functools import cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        d_low, d_high = len(str(low)), len(str(high))
        available_digits = [d for d in range(d_low, d_high + 1) if d % 2 == 0]

        if not available_digits:
            return 0

        @cache
        def dp(l: int, lower_bound, upper_bound: int, remainder: int, even_digit_count: int):
            res = 0

            if l == 1:
                upper_bound = min(upper_bound, pow(10, 2 * l) - 1)
                lower_bound = max(lower_bound, pow(10, 2 * l - 1))

                r_begin = lower_bound % k
                begin = lower_bound - r_begin + remainder + k * int(r_begin > remainder)
                for j in range(begin, upper_bound + 1, k):
                    even_digits = int(j < 10)
                    for digit in str(j):
                        if int(digit) % 2 == 0:
                            even_digits += 1
                    if even_digits == even_digit_count:
                        res += 1
                return res

            for r in range(k):
                prefix_r = r * pow(10, 2 * (l - 1)) % k
                suffix_r = (k + remainder - prefix_r) % k

                prefix_upper_bound = 99
                prefix_lower_bound = 10

                for even_digits in range(0, 3):
                    if even_digits > even_digit_count:
                        break
                    f1 = dp(l - 1, upper_bound + 1, suffix_r, even_digit_count - even_digits)
                    f2 = dp(1, upper_bound, r, even_digits)

                    res += f1 * f2

            return res

        return sum([dp(d // 2, low, high, 0, d // 2) for d in available_digits])


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.number_of_beautiful_integers = Solution().numberOfBeautifulIntegers

    def test_1(self) -> None:
        self.assertEqual(2, self.number_of_beautiful_integers(10, 20, 3))

    def test_2(self) -> None:
        self.assertEqual(1, self.number_of_beautiful_integers(1, 10, 1))

    def test_3(self) -> None:
        self.assertEqual(0, self.number_of_beautiful_integers(5, 5, 2))

    def test_4(self) -> None:
        self.assertEqual(3, self.number_of_beautiful_integers(47, 100, 18))

    def test_5(self) -> None:
        self.assertEqual(2, self.number_of_beautiful_integers(28, 114, 16))

    def test_6(self) -> None:
        self.assertEqual(8203160, self.number_of_beautiful_integers(10000000, 99999999, 3))
