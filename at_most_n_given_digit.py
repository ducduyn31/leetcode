from typing import List


def atMostNGivenDigitSet(digits: List[str], n: int) -> int:
    n_digits = str(n)
    at_most = sum(len(digits) ** i for i in range(1, len(n_digits)))

    def count_available(nth: int) -> int:
        if nth == len(n_digits):
            return 1
        count = 0
        most_significant = n_digits[nth]

        for digit in digits:
            if digit < most_significant:
                count += len(digits) ** (len(n_digits) - nth - 1)

        if most_significant in digits:
            count += count_available(nth + 1)
        return count

    return at_most + count_available(0)


if __name__ == '__main__':
    print(atMostNGivenDigitSet(digits=["1", "2", "3", "4", "5", "6", "7", "9"], n=1))
    print(atMostNGivenDigitSet(digits=["1", "7"], n=231))
    print(atMostNGivenDigitSet(digits=["0", "3", "4", "5", "6"], n=64))
    print(atMostNGivenDigitSet(digits=["3", "4", "5", "6"], n=64))
    print(atMostNGivenDigitSet(digits=["3", "4", "8"], n=4))
    print(atMostNGivenDigitSet(digits=["3", "5"], n=4))
    print(atMostNGivenDigitSet(digits=["1", "3", "5", "7"], n=100))
    print(atMostNGivenDigitSet(digits=["1", "4", "9"], n=1000000000))
    print(atMostNGivenDigitSet(digits=["7"], n=8))
