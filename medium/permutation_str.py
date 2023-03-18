from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    S = defaultdict(int)
    nS = len(s1)
    for c in s1:
        S[c] += 1

    first = last = 0
    while last < len(s2):
        if s2[first] not in S:
            first = last = first + 1
        else:
            if s2[last] in S and S[s2[last]] > 0:
                S[s2[last]] -= 1
                last += 1
                nS -= 1
            else:
                S[s2[first]] += 1
                first += 1
                nS += 1

        if nS == 0:
            return True

    return False


if __name__ == '__main__':
    print(checkInclusion('ab', 'eidbaooo'))
    print(checkInclusion('ab', 'eidboaoo'))
