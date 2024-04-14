from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == '__main__':
    print(isAnagram(s="anagram", t="nagaram"))
    print(isAnagram(s="rat", t="car"))
