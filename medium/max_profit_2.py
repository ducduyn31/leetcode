from typing import List


def maxProfit(prices: List[int]) -> int:
    max_current = 0
    max_diff = 0

    for i in range(1, len(prices)):
        max_current = max(prices[i] - prices[i -1], max_current + prices[i] - prices[i - 1])
        max_diff = max(max_diff, max_current)

    return max_diff


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))
