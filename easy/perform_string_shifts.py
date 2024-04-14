from typing import List


def stringShift(s: str, shift: List[List[int]]) -> str:
    s = list(s)
    m = 0
    l = len(s)
    for direction, amount in shift:
        if direction == 0:
            m -= amount
        else:
            m += amount
    m %= l
    return ''.join(s[l - m:] + s[:l - m])


if __name__ == '__main__':
    print(stringShift('abc', [[0, 0], [0, 0]]))
    print(stringShift('abc', []))
    print(stringShift('abcdefg', [[1, 1], [1, 1], [0, 2], [1, 3]]))
