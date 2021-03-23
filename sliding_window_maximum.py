from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    slider = deque()
    ans = []

    for i in range(k):
        while slider and nums[slider[-1]] <= nums[i]:
            slider.pop()
        slider.append(i)

    for i in range(k, len(nums)):
        ans.append(nums[slider[0]])
        while slider and slider[0] <= i - k:
            slider.popleft()
        while slider and nums[slider[-1]] <= nums[i]:
            slider.pop()
        slider.append(i)

    ans.append(nums[slider[0]])

    return ans


if __name__ == '__main__':
    print(maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3))
    print(maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(maxSlidingWindow(nums=[1], k=1))
    print(maxSlidingWindow(nums=[1, -1], k=1))
    print(maxSlidingWindow(nums=[9, 11], k=2))
    print(maxSlidingWindow(nums=[4, -2], k=2))
