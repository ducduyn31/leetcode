from typing import List


def plusOne(digits: List[int]) -> List[int]:
    c = 1
    k = len(digits) - 1
    while c != 0:
        digits[k] += 1
        c = 0
        if digits[k] == 10:
            digits[k] = 0
            c = 1
            k -= 1
            if k < 0:
                digits.insert(0, 1)
                c = 0

    return digits



if __name__ == '__main__':
    print(plusOne(digits=[1, 2, 3]))
    print(plusOne(digits=[4, 3, 2, 1]))
    print(plusOne(digits=[0]))
    print(plusOne(digits=[9]))
