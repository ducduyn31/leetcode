import unittest


class Solution:

    def findMaxConsecutivePairs(self, s, k):
        # left, right = 0, 0
        # zeros = 0
        # ones = 0
        #
        # while zeros < k and right < len(s):
        #     zeros += s[right] == "0"
        #     ones += s[right] == "1"
        #     right += 1
        #
        # max_pairs = current_pairs = max(0, zeros + ones - (k - zeros) - 1)
        #
        # if right == len(s):
        #     return max_pairs
        #
        # while right < len(s):
        #     zeros += s[right] == "0"
        #     ones += s[right] == "1"
        #
        #     if s[right] == "1":
        #         right += 1
        #     else:
        #         while s[left] == "1":
        #             left += 1
        #             current_pairs -= 1
        #             ones -= 1
        #
        #         zeros -= 1
        #
        #         right += 1
        #
        #     current_pairs = max(0, zeros + ones - (k - zeros) - 1)
        #     max_pairs = max(max_pairs, current_pairs)
        #
        # return max_pairs

        cons = [1]
        idx = [s[0]]

        for i in range(1, len(s)):
            if s[i] == idx[-1]:
                cons[-1] += 1
            else:
                cons.append(1)
                idx.append(s[i])







class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.find_max_consecutive_pairs = Solution().findMaxConsecutivePairs

    def test_1(self):
        s = "01010"
        k = 2
        self.assertEqual(3, self.find_max_consecutive_pairs(s, k))

    def test_2(self):
        s = "101"
        k = 2
        self.assertEqual(1, self.find_max_consecutive_pairs(s, k))

    def test_3(self):
        s = "000"
        k = 2
        self.assertEqual(1, self.find_max_consecutive_pairs(s, k))

    def test_4(self):
        s = "000"
        k = 1
        self.assertEqual(0, self.find_max_consecutive_pairs(s, k))

    def test_5(self):
        s = "111"
        k = 0
        self.assertEqual(2, self.find_max_consecutive_pairs(s, k))

    def test_6(self):
        s = "10001"
        k = 3
        self.assertEqual(4, self.find_max_consecutive_pairs(s, k))

    def test_7(self):
        s = "10101"
        k = 3
        self.assertEqual(3, self.find_max_consecutive_pairs(s, k))

    def test_8(self):
        s = "00000"
        k = 0
        self.assertEqual(0, self.find_max_consecutive_pairs(s, k))

    def test_9(self):
        s = "10001"
        k = 1
        self.assertEqual(1, self.find_max_consecutive_pairs(s, k))

    def test_10(self):
        s = "1000101"
        k = 1
        self.assertEqual(2, self.find_max_consecutive_pairs(s, k))

    def test_11(self):
        s = "1000101"
        k = 2
        self.assertEqual(3, self.find_max_consecutive_pairs(s, k))

    def test_12(self):
        s = "10101"
        k = 5
        self.assertEqual(0, self.find_max_consecutive_pairs(s, k))

    def test_13(self):
        s = "01110"
        k = 4
        self.assertEqual(2, self.find_max_consecutive_pairs(s, k))
