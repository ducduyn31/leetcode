def removeKdigits(num: str, k: int) -> str:
    result = []

    for c in num:
        while k and result and c < result[-1]:
            result.pop()
            k -= 1
        result.append(c)

    while k:
        result.pop()
        k -= 1

    return ''.join(result).lstrip('0') or '0'


if __name__ == '__main__':
    print(removeKdigits('9', 1))
    print(removeKdigits('43214321', 4))
    print(removeKdigits('112', 1))
    print(removeKdigits('1432219', 3))
    print(removeKdigits('10200', 1))
    print(removeKdigits('10', 2))
