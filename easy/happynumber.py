from math import sqrt, floor


def hasSquareRoot(n: int) -> bool:
    return floor(sqrt(n)) ** 2 == n


def isHappy(n: int) -> bool:
    prev = set()

    def is_happy_recur(i: int) -> bool:
        if i == 1:
            return True
        elif i in prev:
            return False
        else:
            prev.add(i)

        new_numer = 0
        while i > 0:
            new_numer += (i % 10) ** 2
            i = i // 10

        return is_happy_recur(new_numer)

    return is_happy_recur(n)


if __name__ == '__main__':
    assert isHappy(19) is True
    assert isHappy(2) is False
    assert isHappy(7) is True
    # isHappy()
