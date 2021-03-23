def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0

    a, b = 1, 1

    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i - 1] == '1' or s[i - 1] == '2':
                b = a
            else:
                return 0
        elif s[i - 1] == '1' or (s[i - 1] == '2' and int(s[i]) <= 6):
            a, b = b, a + b
        else:
            a = b
    return b


if __name__ == '__main__':
    print(numDecodings("230"))
    print(numDecodings("1201234"))
    print(numDecodings('10011'))
    print(numDecodings('2101'))
    print(numDecodings('10'))
    print(numDecodings('12'))
    print(numDecodings('226'))
    print(numDecodings('0'))
