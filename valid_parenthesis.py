def isValid(s: str) -> bool:
    S = []
    symbol_mapper = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in {'(', '[', '{'}:
            S.append(c)
        else:
            if not S:
                return False

            if S[-1] != symbol_mapper[c]:
                return False

            S.pop()
    return len(S) == 0


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))
    print(isValid("]"))
