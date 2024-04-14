from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    term_counter = Counter(s1)

    for i in range(0, len(s2) - len(s1) + 1):
        count = Counter(s2[i:i + len(s1)])

        if term_counter == count:
            return True

    return False


if __name__ == '__main__':
    assert checkInclusion('ab', 'eidbaooo') is True
    assert checkInclusion('ab', 'eidboaoo') is False
    assert checkInclusion('aabc', 'acaab') is True
