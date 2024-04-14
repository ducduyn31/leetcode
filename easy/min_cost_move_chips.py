from typing import List


def minCostToMoveChips(position: List[int]) -> int:
    odd, even = 0, 0
    for pos in position:
        if pos % 2 == 0:
            even += 1
        else:
            odd += 1

    return min(odd, even)


if __name__ == '__main__':
    print(minCostToMoveChips([1, 2, 3]))
    print(minCostToMoveChips([2, 2, 2, 3, 3]))
    print(minCostToMoveChips([1, 1000000000]))
