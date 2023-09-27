import unittest
from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1

        n = max(max(nums).bit_length(), target.bit_length())
        required_idx = deque()
        state = [0] * n
        t = target
        for i in range(n - 1, -1, -1):
            if 1 & t:
                required_idx.append(i)
            t >>= 1

        last_num = 0
        prev_state = 0
        for i in nums:
            state[-i.bit_length()] += 1
            last_num = max(last_num, n - i.bit_length())

        ans = 0
        while required_idx:
            lsb = required_idx[0]

            if lsb <= last_num:
                while lsb <= last_num:
                    new_state = state[last_num] + prev_state
                    if lsb == last_num and new_state > 0:
                        required_idx.popleft()
                        new_state -= 1
                    prev_state, updated_state = divmod(new_state, 2)
                    state[last_num] = updated_state
                    last_num -= 1

            else:
                while last_num >= 0 and lsb == required_idx[0]:
                    if state[last_num] > 0:
                        while required_idx and required_idx[0] > last_num:
                            required_idx.popleft()
                        ans += lsb - last_num
                        state[last_num] -= 1
                        break
                    last_num -= 1

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
