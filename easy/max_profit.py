from typing import List


def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0

    transactions = []

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            transactions.append(prices[i] - prices[i - 1])

    return sum(transactions)


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([1, 2, 3, 4, 5]))
    print(maxProfit([7, 6, 4, 3, 1]))
    print(maxProfit([1, 2]))
