def hammingDistance(x: int, y: int) -> int:
    ans = 0

    while x != y:
        if (x - y) % 2 == 1:
            ans += 1
        x >>= 1
        y >>= 1

    return ans


if __name__ == '__main__':
    print(hammingDistance(93, 73))
    print(hammingDistance(1, 4))
