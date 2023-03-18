def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    last_position = {}
    substr_head = 0
    for i, character in enumerate(s):
        if character in last_position:
            substr_head = max(last_position[character] + 1, substr_head)
        longest = max(longest, i - substr_head + 1)

        # Update pace
        last_position[character] = i

    return longest


if __name__ == '__main__':
    assert lengthOfLongestSubstring('abcabcbb') == 3
    assert lengthOfLongestSubstring('bbbbb') == 1
    assert lengthOfLongestSubstring('pwwkew') == 3
    assert lengthOfLongestSubstring('aab') == 2
    assert lengthOfLongestSubstring('tmmzuxt') == 5
