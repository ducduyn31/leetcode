import random
from typing import List


def clazz_runner(steps: List[str], parameters: List[List], out):
    obj = globals()[steps[0]](*parameters[0])
    steps.pop(0)
    parameters.pop(0)

    for f, a in zip(steps, parameters):
        ret_value = getattr(obj, f)(*a)
        if ret_value and out:
            out(ret_value)


class Solution:

    def __init__(self, nums: List[int]):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))


if __name__ == '__main__':
    clazz_runner(["Solution", "shuffle", "reset", "shuffle"], [[[1, 2, 3]], [], [], []], print)
