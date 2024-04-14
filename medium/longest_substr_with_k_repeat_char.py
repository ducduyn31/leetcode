from collections import defaultdict


def longestSubstring(s: str, k: int) -> int:
    longest = 0

    for max_current_chars_in_substr in range(1, len(set(s)) + 1):
        start, end = 0, 0
        current_chars = defaultdict(int)
        count_k = 0

        while end < len(s):
            if len(current_chars) <= max_current_chars_in_substr:
                current_chars[s[end]] += 1
                if current_chars[s[end]] == k:
                    count_k += 1
                end += 1
            else:
                if current_chars[s[start]] == k:
                    count_k -= 1
                current_chars[s[start]] -= 1
                if current_chars[s[start]] == 0:
                    del current_chars[s[start]]
                start += 1

            if len(current_chars) == max_current_chars_in_substr and count_k == max_current_chars_in_substr:
                longest = max(longest, end - start)

    return longest


if __name__ == '__main__':
    print(longestSubstring(s="aaabbb", k=3))
    print(longestSubstring(s="ababacb", k=3))
    print(longestSubstring(s="aaabb", k=3))
    print(longestSubstring(s="ababbc", k=2))
