def myAtoi(s: str) -> int:
    s = s.strip()
    if not s[0].isdigit() and not s[0] == '+' and not s[0] == '-':
        return 0
    if not s:
        return 0
    sign = -1 if s[0] == '-' else 1
    skip = 1 if s[0] == '-' or s[0] == '+' else 0
    r = ['0']
    for c in s[skip:]:
        if c.isdigit():
            r.append(c)
        else:
            break

    i = int(''.join(r))
    if i > 2147483647:
        return 2147483647 if sign == 1 else -2147483648

    return sign * i


if __name__ == '__main__':
    print(myAtoi("42"))
    print(myAtoi("   -42"))
    print(myAtoi("   -42 dfd3"))
    print(myAtoi("4193 with words"))
    print(myAtoi("words and 987"))
    print(myAtoi("-91283472332"))
    print(myAtoi("3.14159"))
    print(myAtoi("+-12"))
