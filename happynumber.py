from math import sqrt, floor


def hasSquareRoot(n: int) -> bool:
    return floor(sqrt(n)) ** 2 == n


def isHappy(n: int) -> bool:
    map = set()

    current = n

    while current not in map and current > 1:
        map.add(current)
        sum = 0
        while current != 0:
            sum += (current % 10) ** 2
            current = current // 10

        if sum == 1:
            return True

        current = sum

    return False


if __name__ == '__main__':
    print(isHappy(18))
    # isHappy()
