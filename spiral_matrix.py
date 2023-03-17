from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    x, y = 0, 0
    inc_x, inc_y = 1, 0
    max_y, max_x = len(matrix) - 1, len(matrix[0]) - 1
    min_y, min_x = 1, 0
    result = []

    while len(result) < len(matrix) * len(matrix[0]):
        result.append(matrix[y][x])

        # Update increment
        if inc_x == 1 and x == max_x:
            inc_x = 0
            inc_y = 1
            max_x -= 1
        elif inc_x == -1 and x == min_x:
            inc_x = 0
            inc_y = -1
            min_x += 1
        elif inc_y == 1 and y == max_y:
            inc_y = 0
            inc_x = -1
            max_y -= 1
        elif inc_y == -1 and y == min_y:
            inc_y = 0
            inc_x = 1
            min_y += 1

        # Update location
        x += inc_x
        y += inc_y

    return result


if __name__ == '__main__':
    assert spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
