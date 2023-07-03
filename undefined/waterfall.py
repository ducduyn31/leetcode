from typing import Callable


class SequentialFunctionWrapper:

    def __init__(self, func: Callable, *args, **kwargs):
        self._do_func = func
        self.args = args
        self.kwargs = kwargs

        self.returned_value = func(*args, **kwargs)
        while isinstance(self.returned_value, SequentialFunctionWrapper):
            self.returned_value = self.returned_value.value()

    def then(self, then_func):
        return SequentialFunctionWrapper(then_func, self.returned_value)

    def value(self):
        return self.returned_value

    def __str__(self):
        return str(self.value())


def waterfall(func):
    def wrapper(*args, **kwargs):
        return SequentialFunctionWrapper(func, *args, **kwargs)

    return wrapper


@waterfall
def add(a, b):
    return a + b


@waterfall
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    v1 = add(1,2)
    print(v1)
    v2 = v1.then(lambda x: multiply(x, 2))
    print(v2)
    v3 = v2.then(lambda x: add(x, 5))
    print(v3)