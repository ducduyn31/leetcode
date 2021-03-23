from typing import List


def reverseString(s: List[str]) -> None:
    n = len(s)
    for i in range(len(s) // 2):
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)
    s = ["H", "a", "n", "n", "a", "h"]
    reverseString(s)
    print(s)
