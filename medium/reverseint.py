def reverse(x: int) -> int:
    result = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])

    if result > 2 ** 31 - 1 or result < -2 ** 31:
        return 0
    return result


if __name__ == '__main__':
    input = 123
    print(reverse(input))

    input = -123
    print(reverse(input))

    input = 120
    print(reverse(input))

    input = -10
    print(reverse(input))
