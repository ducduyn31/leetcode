from typing import List


def clazz_runner(steps: List[str], parameters: List[List], out):
    obj = globals()[steps[0]](*parameters[0])
    steps.pop(0)
    parameters.pop(0)

    for f, a in zip(steps, parameters):
        ret_value = getattr(obj, f)(*a)
        if ret_value and out:
            out(ret_value)


class FirstUnique:

    def __init__(self, nums: List[int]):
        pass

    def showFirstUnique(self) -> int:
        pass

    def add(self, value: int) -> None:
        pass
