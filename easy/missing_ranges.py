from typing import List


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    ans = []

    def insert_range_str(start, end):
        if start == end:
            ans.append(f'{start}')
        if start < end:
            ans.append(f'{start}->{end}')

    if not nums:
        insert_range_str(lower, upper)
        return ans

    for n in nums:
        if lower == n:
            lower = lower + 1
            continue
        insert_range_str(lower, n - 1)
        lower = n + 1

    insert_range_str(lower, upper)

    return ans


if __name__ == '__main__':
    print(findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))
    print(findMissingRanges(nums=[], lower=1, upper=1))
    print(findMissingRanges(nums=[], lower=-3, upper=-1))
    print(findMissingRanges(nums=[-1], lower=-1, upper=-1))
    print(findMissingRanges(nums=[-1], lower=-2, upper=-1))
