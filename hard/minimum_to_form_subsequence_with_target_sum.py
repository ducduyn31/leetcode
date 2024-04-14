import unittest
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target:
            return -1

        nums.sort()
        ans = 0
        while target > 0:
            current = nums.pop()
            if total - current >= target:
                total -= current
            elif current <= target:
                total -= current
                target -= current
            else:
                nums.append(current // 2)
                nums.append(current // 2)
                ans += 1

        return ans


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.min_operations = Solution().minOperations

    def test_1(self):
        self.assertEqual(1, self.min_operations([1, 2, 8], 7))

    def test_2(self):
        self.assertEqual(2, self.min_operations([1, 32, 1, 2], 12))

    def test_3(self):
        self.assertEqual(-1, self.min_operations([1, 32, 1], 35))

    def test_4(self):
        self.assertEqual(1, self.min_operations([128, 8, 8, 2], 4))

    def test_5(self):
        self.assertEqual(1, self.min_operations(
            [128, 1024, 1073741824, 4194304, 268435456, 1024, 16, 1073741824, 131072, 4, 16777216, 67108864, 16777216,
             268435456, 1073741824, 256, 16, 67108864, 1048576, 16, 4, 4194304, 1024, 16, 262144, 1048576, 1024, 128,
             1073741824, 67108864, 65536, 128, 32768, 128, 32768, 8192, 256, 1024], 38))
