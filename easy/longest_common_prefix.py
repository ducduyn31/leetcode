from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs or not strs[0]:
        return ''

    min_str = min(strs, key=len)

    for i, c in enumerate(min_str):
        for s in strs:
            if s[i] != c:
                return min_str[:i]

    return min_str


if __name__ == '__main__':
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog", "racecar", "car"]))
    print(longestCommonPrefix([]))
    print(longestCommonPrefix([""]))
    print(longestCommonPrefix(["a"]))
    print(longestCommonPrefix(["ab", "a"]))
