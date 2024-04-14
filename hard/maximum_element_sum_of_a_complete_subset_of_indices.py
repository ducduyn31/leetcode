import unittest
from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        is_prime = [True] * (len(nums) + 1)
        primes = []
        p = 2
        while p * p <= len(nums) + 1:
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, len(is_prime), p):
                    is_prime[i] = False
            p += 1

        def group_product(x: int):
            group = 1

            for p in primes:
                factor_count = 0

                while x % p == 0:
                    x //= p
                    factor_count += 1

                if factor_count % 2 == 1:
                    group *= p

            return group * x

        groups = defaultdict(int)
        max_value = 0

        for i in range(1, len(nums) + 1):
            group = group_product(i)
            groups[group] += nums[i - 1]
            max_value = max(max_value, groups[group])

        return max_value


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.maximum_sum = Solution().maximumSum

    def test_1(self) -> None:
        self.assertEqual(self.maximum_sum([8, 7, 3, 5, 7, 2, 4, 9]), 16)

    def test_2(self) -> None:
        self.assertEqual(self.maximum_sum([5, 10, 3, 10, 1, 13, 7, 9, 4]), 19)

    def test_3(self) -> None:
        self.assertEqual(self.maximum_sum([1, 1, 1, 1]), 2)
