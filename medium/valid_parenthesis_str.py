def checkValidString(s: str) -> bool:
    lo, hi = 0, 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += -1 if c == ')' else 1
        if hi < 0:
            break
        lo = max(lo, 0)

    return lo == 0


if __name__ == '__main__':
    print(checkValidString('*)()*'))
    print(checkValidString(''))
    print(checkValidString('()'))
    print(checkValidString(')('))
    print(checkValidString(')()*'))
    print(checkValidString('(*)'))
    print(checkValidString('(*))'))
    print(checkValidString('(*()'))
