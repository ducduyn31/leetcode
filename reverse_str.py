from typing import List


def reverseString(s: List[str]) -> None:
    n = len(s)
    for i in range(len(s) // 2):
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


def assert_reverse(s: List[str], result: List[str]):
    reverseString(s)
    assert s == result


if __name__ == '__main__':
    assert_reverse(["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"])
    assert_reverse(["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
