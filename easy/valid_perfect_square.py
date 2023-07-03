def isPerfectSquare(num: int) -> bool:
    temp = 0
    diff = 1

    while temp + diff <= num:
        temp += diff
        diff += 2

    return temp == num


if __name__ == '__main__':
    print(isPerfectSquare(1))
    print(isPerfectSquare(16))
    print(isPerfectSquare(14))
