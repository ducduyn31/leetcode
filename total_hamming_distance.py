from typing import List


def totalHammingDistanceForSpaceEfficiency(nums: List[int]) -> int:
    distance = 0
    n = len(nums)
    for _ in range(32):
        odd = 0
        for i in range(n):
            odd += nums[i] & 1
            nums[i] >>= 1
        distance += odd * (n - odd)

    return distance


def totalHammingDistance(nums: List[int]) -> int:
    dist, n = 0, len(nums)
    for s in zip(*map('{:032b}'.format, nums)):
        x = s.count('0')
        dist += x * (n-x)

    return dist



if __name__ == '__main__':
    print(totalHammingDistance([4, 14, 2]))
