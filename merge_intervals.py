from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    ans = [intervals[0]]

    for interval in intervals:
        if interval[0] > ans[-1][1]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans


if __name__ == '__main__':
    print(merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]))
    print(merge([[1, 4], [0, 2], [3, 5]]))
    print(merge([[1, 4], [5, 6]]))
    print(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
    print(merge([[1, 4], [2, 3]]))
    print(merge([[1, 4], [0, 4]]))
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge([[1, 4], [4, 5]]))
