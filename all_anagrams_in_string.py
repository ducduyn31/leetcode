from collections import defaultdict
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    result = []

    P = defaultdict(int)
    nP = len(p)
    for c in p:
        P[c] += 1

    first = last = 0

    while last < len(s):
        if s[first] not in P:
            first = last = first + 1
        else:
            if s[last] in P and P[s[last]] > 0:
                P[s[last]] -= 1
                last += 1
                nP -= 1
            else:
                P[s[first]] += 1
                first += 1
                nP += 1

        if nP == 0:
            result.append(first)

    return result


if __name__ == '__main__':
    print(findAnagrams('ecbaebabacd', 'abc'))
    print(findAnagrams('cbaebabacd', 'abc'))
    print(findAnagrams('abab', 'ab'))
