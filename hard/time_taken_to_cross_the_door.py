import unittest
from collections import deque
from typing import List


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enter_queue = deque()
        exit_queue = deque()

        for i, (time, is_exit) in enumerate(zip(arrival, state)):
            if is_exit == 1:
                exit_queue.append(i)
            else:
                enter_queue.append(i)

        pass_order = []
        result = [0] * len(arrival)

        if exit_queue and arrival[exit_queue[0]] == arrival[0]:
            next_pass = exit_queue.popleft()
            pass_order.append((next_pass, arrival[next_pass]))
        else:
            next_pass = enter_queue.popleft()
            pass_order.append((next_pass, arrival[next_pass]))

        while exit_queue or enter_queue:
            last_pass, pass_time = pass_order[-1]

            if enter_queue \
                    and arrival[enter_queue[0]] - pass_time <= 1 \
                    and state[last_pass] == 0:
                next_pass = enter_queue.popleft()
                pass_order.append((next_pass, max(arrival[next_pass], pass_time + 1)))
                continue
            if exit_queue \
                    and arrival[exit_queue[0]] - pass_time <= 1 \
                    and state[last_pass] == 1:
                next_pass = exit_queue.popleft()
                pass_order.append((next_pass, max(arrival[next_pass], pass_time + 1)))
                continue

            if enter_queue and exit_queue and arrival[exit_queue[0]] <= arrival[enter_queue[0]]:
                next_pass = exit_queue.popleft()
                pass_order.append((next_pass, max(arrival[next_pass], pass_time + 1)))
            elif enter_queue and exit_queue:
                next_pass = enter_queue.popleft()
                pass_order.append((next_pass, max(arrival[next_pass], pass_time + 1)))

            if not enter_queue:
                while exit_queue:
                    last_pass, pass_time = pass_order[-1]
                    next_pass = exit_queue.popleft()
                    pass_order.append((next_pass, max(arrival[next_pass], pass_time + 1)))

            if not exit_queue:
                while enter_queue:
                    last_pass, pass_time = pass_order[-1]
                    next_pass = enter_queue.popleft()
                    pass_order.append((next_pass, max(arrival[next_pass], pass_time + 1)))

        for order, time in pass_order:
            result[order] = time

        return result


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.time_taken = Solution().timeTaken

    def test_time_take_should_return_0_3_1_2_4(self):
        self.assertListEqual([0, 3, 1, 2, 4], self.time_taken([0, 1, 1, 2, 4], [0, 1, 0, 0, 1]))

    def test_time_take_should_return_0_2_1(self):
        self.assertListEqual([0, 2, 1], self.time_taken([0, 0, 0], [1, 0, 1]))

    def test_time_take_should_return_3_6_4_7_5_8(self):
        self.assertListEqual([3, 6, 4, 7, 5, 8], self.time_taken([3, 3, 4, 5, 5, 5], [1, 0, 1, 0, 1, 0]))

    def test_time_take_should_return_from_0_to_21(self):
        self.assertListEqual([0, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 11, 17, 18, 20, 19, 21],
                             self.time_taken([0, 5, 6, 6, 7, 9, 9, 9, 10, 10, 10, 10, 10, 15, 16, 17, 17, 17],
                                             [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0]))
