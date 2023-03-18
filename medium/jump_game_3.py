from typing import List


def canReach(arr: List[int], start: int) -> bool:
    Q = [start]
    traversed = set()

    while Q:
        current_index = Q.pop(0)
        if current_index in traversed:
            continue
        if arr[current_index] == 0:
            return True
        traversed.add(current_index)
        if current_index + arr[current_index] < len(arr):
            Q.append(current_index + arr[current_index])
        if current_index - arr[current_index] >= 0:
            Q.append(current_index - arr[current_index])

    return False


if __name__ == '__main__':
    print(canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
    print(canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
    print(canReach(arr=[3, 0, 2, 1, 2], start=2))
