def removeDuplicates(s: str, k: int) -> str:
    result = []

    for c in s:
        if not result:
            result.append([c, 1])
            continue

        if result[-1][0] == c and result[-1][1] == k - 1:
            result.pop()
        elif result[-1][0] == c:
            result[-1][1] += 1
        else:
            result.append([c, 1])

    return ''.join(map(lambda e: e[0] * e[1], result))


if __name__ == '__main__':
    print(removeDuplicates('abcd', 2))
    print(removeDuplicates('deeedbbcccbdaa', 3))
    print(removeDuplicates('pbbcggttciiippooaais', 2))
