import unittest


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        stack = []

        for c in num:
            if not stack:
                stack.append(c)
            else:
                while stack and ord(stack[-1]) > ord(c) and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(c)

        while k > 0:
            stack.pop()
            k -= 1

        return "".join(stack).lstrip("0") or "0"


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.remove_kdigits = Solution().removeKdigits

    def test_1(self):
        num = "1432219"
        k = 3
        self.assertEqual(self.remove_kdigits(num, k), "1219")

    def test_2(self):
        num = "10200"
        k = 1
        self.assertEqual(self.remove_kdigits(num, k), "200")

    def test_3(self):
        num = "10"
        k = 2
        self.assertEqual(self.remove_kdigits(num, k), "0")

    def test_4(self):
        num = "112"
        k = 1
        self.assertEqual(self.remove_kdigits(num, k), "11")

    def test_5(self):
        num = "1234567890"
        k = 9
        self.assertEqual(self.remove_kdigits(num, k), "0")

    def test_6(self):
        num = "1432219"
        k = 4
        self.assertEqual(self.remove_kdigits(num, k), "119")

    def test_7(self):
        num = "52660469"
        k = 2
        self.assertEqual(self.remove_kdigits(num, k), "260469")
