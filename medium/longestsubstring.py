def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    map = {}
    head = 0

    for i, c in enumerate(s):
        if c in map:
            head = max(map[c] + 1, head)

        map[c] = i
        longest = max(longest, i - head + 1)

    return longest


if __name__ == '__main__':
    input = 'abcabcbb'
    print(lengthOfLongestSubstring(input))

    input = 'bbbbb'
    print(lengthOfLongestSubstring(input))

    input = 'pwwkew'
    print(lengthOfLongestSubstring(input))

    input = 'aab'
    print(lengthOfLongestSubstring(input))

    input = 'tmmzuxt'
    print(lengthOfLongestSubstring(input))
