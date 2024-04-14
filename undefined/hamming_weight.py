def hammingWeight(n: int) -> int:
    return '{0:b}'.format(n).count('1')

if __name__ == '__main__':
    print(hammingWeight(int('00000000000000000000000000001011', 2)))
    print(hammingWeight(int('00000000000000000000000010000000', 2)))
    print(hammingWeight(int('11111111111111111111111111111101', 2)))