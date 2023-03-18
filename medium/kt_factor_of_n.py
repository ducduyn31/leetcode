def kthFactor(n: int, k: int) -> int:
    for i in range(1, n + 1):
        if n % i == 0:
            k -= 1
            if k == 0:
                return i

    return -1


if __name__ == '__main__':
    print(kthFactor(12, 3))
    print(kthFactor(7, 2))
    print(kthFactor(4, 4))
    print(kthFactor(1, 1))
    print(kthFactor(1000, 3))
