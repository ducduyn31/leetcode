from typing import List


def countElements(arr: List[int]) -> int:
    elements = dict()
    count = 0

    for i in range(len(arr)):
        n = elements.get(arr[i], 0)
        elements[arr[i]] = n + 1

    for i in elements:
        if i + 1 in elements:
            count += elements[i]

    return count


if __name__ == '__main__':
    input = [1, 2, 3]
    print(countElements(input))

    input = [1, 1, 3, 3, 5, 5, 7, 7]
    print(countElements(input))

    input = [1, 3, 2, 3, 5, 0]
    print(countElements(input))

    input = [1, 1, 2, 2]
    print(countElements(input))

    input = [1, 1, 2]
    print(countElements(input))
