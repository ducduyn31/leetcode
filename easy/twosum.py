from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):

            subtracted = target - num

            if subtracted not in map:
                map[num] = i
            else:
                return [map[subtracted], i]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 5, 5, 11], 10))
    print(s.twoSum([-3, 4, 3, 90], 0))
    # s.twoSum([2,5,5,11], 10)
