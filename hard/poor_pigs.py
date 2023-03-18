from math import ceil, log


def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    T = minutesToTest // minutesToDie
    k = 0
    while (T + 1) ** k < buckets:
        k += 1
    return k


if __name__ == '__main__':
    print(poorPigs(1000, 15, 60))
    print(poorPigs(10, 15, 15))
    print(poorPigs(10, 15, 30))
