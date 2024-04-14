from typing import List


def findSpecialInteger(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]

    for i in range(3 * len(arr) // 4):
        if arr[i] == arr[i + len(arr) // 4]:
            return arr[i]



if __name__ == '__main__':
    print(findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
    print(findSpecialInteger([1, 2, 2, 3, 4, 6, 6, 6, 6]))
