import heapq
from typing import List


def kthSmallest(mat: List[List[int]], k: int) -> int:
    def kthSmallestPair(nums1: List[int], nums2: List[int], k: int):
        h = []
        res = []

        i = 0
        while i < len(nums1) and i < k:
            heapq.heappush(h, (nums1[i] + nums2[0], nums1[i], 0))
            i += 1

        while k > 0 and h:
            current = heapq.heappop(h)
            res.append(current[0])

            if current[2] == len(nums2) - 1:
                continue

            heapq.heappush(h, (current[1] + nums2[current[2] + 1], current[1], current[2] + 1))
            k -= 1

        return res

    res = mat[0]

    for r in range(1, len(mat)):
        res = kthSmallestPair(res, mat[r], k)

    return res[k - 1]


if __name__ == '__main__':
    print(kthSmallest([[1, 3, 11],
                       [2, 4, 6]], 5))
    print(kthSmallest([[1, 3, 11],
                       [2, 4, 6]], 9))
    print(kthSmallest([[1, 10, 10],
                       [1, 4, 5],
                       [2, 3, 6]], 7))
    print(kthSmallest([[1, 1, 10],
                       [2, 2, 9]], 7))
