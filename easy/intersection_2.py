from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    count1, count2 = Counter(nums1), Counter(nums2)
    set1, set2 = set(nums1), set(nums2)
    intersected_el = set1.intersection(set2)
    result = []
    for e in intersected_el:
        for _ in range(min(count1.get(e), count2.get(e))):
            result.append(e)
    return result


if __name__ == '__main__':
    print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
