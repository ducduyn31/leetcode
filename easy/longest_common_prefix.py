from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    min_str_id, min_str = min(enumerate(strs), key=lambda pair: len(pair[1]))
    strs.pop(min_str_id)

    if len(strs) == 0:
        return min_str

    def share_prefix(prefix: str) -> bool:
        return all([s[:len(prefix)] == prefix for s in strs])

    low, high = 0, len(min_str)
    prefix_len = 0

    while low <= high:
        mid = (low + high) // 2

        if share_prefix(min_str[:mid]):
            low = mid + 1
            prefix_len = mid
        else:
            high = mid - 1

    return min_str[:prefix_len]


if __name__ == '__main__':
    assert longestCommonPrefix(["ab", "a"]) == 'a'
    assert longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ''
    assert longestCommonPrefix([""]) == ''
    assert longestCommonPrefix(["a"]) == 'a'
