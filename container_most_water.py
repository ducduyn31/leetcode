from typing import List


def maxArea(height: List[int]) -> int:
    ptr1 = 0
    ptr2 = len(height) - 1

    max_area = -1

    while ptr1 != ptr2:
        area = (ptr2 - ptr1)

        if height[ptr1] < height[ptr2]:
            area *= height[ptr1]
            ptr1 += 1
        else:
            area *= height[ptr2]
            ptr2 -= 1

        max_area = max(area, max_area)

    return max_area


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
