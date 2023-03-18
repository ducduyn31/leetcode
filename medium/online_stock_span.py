from typing import List


def clazz_runner(steps: List[str], parameters: List[List], out):
    obj = globals()[steps[0]](*parameters[0])
    steps.pop(0)
    parameters.pop(0)

    for f, a in zip(steps, parameters):
        ret_value = getattr(obj, f)(*a)
        if ret_value and out:
            out(ret_value)


class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append((price, 1))
            return 1

        span = 1
        while self.prices and self.prices[-1][0] <= price:
            span += self.prices.pop()[1]
        self.prices.append((price, span))

        return span


if __name__ == '__main__':
    clazz_runner(["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
                 [[], [100], [80], [60], [70], [60], [75], [85]], print)

    clazz_runner(["StockSpanner", "next", "next", "next", "next", "next"],
                 [[], [31], [41], [48], [59], [79]], print)
