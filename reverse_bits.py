def reverseBits(n: int) -> int:
    return int('{0:032b}'.format(n)[::-1], 2)


if __name__ == '__main__':
    print(reverseBits(int('00000010100101000001111010011100', 2)))
    print(reverseBits(int('11111111111111111111111111111101', 2)))