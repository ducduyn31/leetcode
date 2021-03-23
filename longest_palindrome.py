def longestPalindrome(s: str) -> str:
    t = '%s%s%s' % ('#', '#'.join(list(s)), '#')

    C, R, rad = 0, -1, 0
    P = [0 for _ in range(len(t))]

    for i in range(len(t)):
        if i <= R:
            rad = min(P[2 * C - i], R - i)
        else:
            rad = 0

        while i + rad < len(t) and i - rad >= 0 and t[i - rad] == t[i + rad]:
            rad += 1

        P[i] = rad

        if i + rad - 1 > R:
            C = i
            R = i + rad - 1


    temp = (-1, 0)
    for i, n in enumerate(P):
        if temp[1] < n:
            temp = (i, n)

    return t[temp[0]- P[temp[0]] + 1: temp[0] + P[temp[0]]].replace('#', '')


if __name__ == '__main__':
    input = 'babad'
    print(longestPalindrome(input))

    input = 'cbbd'
    print(longestPalindrome(input))
