from typing import List


def trap(height: List[int]) -> int:
    if len(height) < 2:
        return 0
    water = 0
    left_id, right_id = 0, len(height) - 1
    left, right = height[left_id], height[right_id]

    while left_id < right_id:
        if left <= right:
            left_id += 1
            left = max(left, height[left_id])
            water += left - height[left_id]
        else:
            right_id -= 1
            right = max(right, height[right_id])
            water += right - height[right_id]

    return water


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap([4, 2, 0, 3, 2, 5]))
