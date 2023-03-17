from math import sqrt, ceil


def consecutiveNumbersSum(N: int) -> int:
    # odd_pairs, even_pairs = 0, 0
    #
    # for pair in range(1, N + 1, 2):
    #     if N % pair == 0 and N // pair >= pair // 2:
    #         odd_pairs += 1
    #     # else:
    #     #     break
    #
    # for pair in range(2, N, 2):
    #     if (N - 1) % pair == 0 and (N - pair // 2) // pair > pair // 2:
    #         even_pairs += 1
    #     # else:
    #     #     break
    #
    # return odd_pairs + even_pairs

    count = 0

    for i in range(1, ceil(sqrt(2 * N))):
        num = N - (i * (i - 1) // 2)
        if num % i == 0:
            print(i)
            count += 1

    return count

if __name__ == '__main__':
    print(consecutiveNumbersSum(51))
    print(consecutiveNumbersSum(1))
    print(consecutiveNumbersSum(9))
    print(consecutiveNumbersSum(15))
    print(consecutiveNumbersSum(5))
