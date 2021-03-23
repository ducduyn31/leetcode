import string


def firstUniqChar(s: str) -> int:
    ls = []

    for c in string.ascii_lowercase:
        if s.count(c) == 1:
            ls.append(s.index(c))

    return min(ls) if len(ls) != 0 else -1


if __name__ == '__main__':
    print(firstUniqChar('leetcode'))
    print(firstUniqChar('loveleetcode'))
