from typing import List


def partitionLabels(S: str) -> List[int]:
    positions = {ch: pos for pos, ch in enumerate(S)}

    ans = []
    start = 0

    while start < len(S):
        begin = start
        last = start

        while begin <= last:
            ch = S[begin]
            last = max(last, positions[ch])
            begin += 1

        ans.append(last - start + 1)
        start = begin

    return ans

if __name__ == '__main__':
    print(partitionLabels('ababcbacadefegdehijhklij'))
