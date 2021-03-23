class MinStack:
    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if len(self._min) == 0 or self._min[-1] >= x:
            self._min.append(x)

    def pop(self) -> None:
        x = self._stack.pop()
        if x == self._min[-1]:
            self._min.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)

    print(minStack.getMin())

    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
