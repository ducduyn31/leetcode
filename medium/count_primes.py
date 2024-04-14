def countPrimes(n: int) -> int:
    s = list(range(2, n))

    for i, x in enumerate(s):
        if x != i + 2:
            continue

        r = i

        while r < n - 2:
            s[r] = x
            r += x

    return len(set(s))


if __name__ == '__main__':
    print(countPrimes(2))
    print(countPrimes(10))
    print(countPrimes(0))
    print(countPrimes(1))
