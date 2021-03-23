def rangeBitwiseAnd(m: int, n: int) -> int:
    diff = n - m
    shift = 0
    while diff:
        diff >>= 1
        shift += 1
    m >>= shift
    n >>= shift
    return (m & n) << shift


if __name__ == '__main__':
    print(rangeBitwiseAnd(15, 24))
    print(rangeBitwiseAnd(8, 13))
    print(rangeBitwiseAnd(5, 12))
    print(rangeBitwiseAnd(2, 6))
    print(rangeBitwiseAnd(8, 12))
    print(rangeBitwiseAnd(5, 7))
    print(rangeBitwiseAnd(0, 1))
