from collections import Counter
from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    results = []

    def backtrack(current: List[int], counter):
        if len(current) == len(nums):
            results.append(current[:])
            return

        for n in counter:
            if counter[n] > 0:
                current.append(n)
                counter[n] -= 1

                backtrack(current, counter)

                counter[n] += 1
                current.pop()

    backtrack([], Counter(nums))

    return results


if __name__ == '__main__':
    print(permuteUnique([1, 1, 2]))
    print(permuteUnique([1, 2, 3]))
