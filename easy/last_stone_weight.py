import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-w for w in stones]

    heapq.heapify(stones)

    while len(stones) > 1:
        large_boulder = heapq.heappop(stones)
        small_boulder = heapq.heappop(stones)

        if large_boulder - small_boulder != 0:
            heapq.heappush(stones, large_boulder - small_boulder)

    return -stones[0] if stones else 0

if __name__ == '__main__':
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
