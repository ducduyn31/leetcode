def findComplement(num: int) -> int:
    mask = 1
    n = num

    while num > 1:
        num >>= 1
        mask <<= 1
        mask += 1
    return n ^ mask


if __name__ == '__main__':
    print(findComplement(5))
    print(findComplement(4))
    print(findComplement(3))
    print(findComplement(2))
    print(findComplement(1))
    print(findComplement(0))
