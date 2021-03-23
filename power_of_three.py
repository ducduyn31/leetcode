def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    return 1162261467 % n == 0


if __name__ == '__main__':
    print(isPowerOfThree(81))
    print(isPowerOfThree(27))
    print(isPowerOfThree(0))
    print(isPowerOfThree(9))
    print(isPowerOfThree(45))