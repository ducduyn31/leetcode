from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)

    if m > n:
        nums1, nums2 = nums2, nums1
        m, n = n, m

    M_min, M_max = 0, m

    while M_min <= M_max:
        M = (M_min + M_max) // 2
        N = (m + n + 1) // 2 - M

        if M > M_min and nums1[M - 1] > nums2[N]:
            M_max = M - 1
        elif M < M_max and nums1[M] < nums2[N - 1]:
            M_min = M + 1
        else:
            if M == 0:
                max_left = nums2[N - 1]
            elif N == 0:
                max_left = nums1[M - 1]
            else:
                max_left = max(nums1[M - 1], nums2[N - 1])

            if (m + n) % 2 == 1:
                return float(max_left)

            if M == m:
                min_right = nums2[N]
            elif N == n:
                min_right = nums1[M]
            else:
                min_right = min(nums1[M], nums2[N])

            return (max_left + min_right) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1, nums2))

    nums1 = []
    nums2 = [1]
    print(findMedianSortedArrays(nums1, nums2))
