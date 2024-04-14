import unittest


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)
        modulo = 1_000_000_007

        def find_rotate():
            count = 0
            i = 0
            while i < n:
                if t[:i] == s[-i:] and t[i:] == s[:n - i]:
                    count += 1
                i += 1

            return count

        def count_for_each_index(k_):
            return (pow(n - 1, k_, modulo) - pow(-1, k_)) * pow(n, -1, modulo)

        result = 0
        if s == t:
            result += (n - 1) * count_for_each_index(k - 1)
        f1 = find_rotate()
        result += count_for_each_index(k) * f1

        return result % modulo


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.number_of_ways = Solution().numberOfWays

    def test_example_1(self) -> None:
        s = "abcd"
        t = "cdab"
        k = 2
        self.assertEqual(self.number_of_ways(s, t, k), 2)

    def test_example_2(self) -> None:
        s = "ababab"
        t = "ababab"
        k = 1
        self.assertEqual(self.number_of_ways(s, t, k), 2)

    def test_example_3(self) -> None:
        s = "ceoceo"
        t = "eoceoc"
        k = 4
        self.assertEqual(self.number_of_ways(s, t, k), 208)

    def test_example_4(self) -> None:
        s = "goxoq"
        t = "dfqgl"
        k = 244326024901249
        self.assertEqual(self.number_of_ways(s, t, k), 0)

    def test_example_5(self) -> None:
        s = "ib"
        t = "ib"
        k = 10
        self.assertEqual(self.number_of_ways(s, t, k), 1)
