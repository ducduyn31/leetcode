from typing import List


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    if len(coordinates) <= 2:
        return True

    if coordinates[1][0] - coordinates[0][0] == 0:
        for i in range(2, len(coordinates)):
            x, _ = coordinates[i]
            if x != coordinates[0][0]:
                return False
    else:
        a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        b = coordinates[0][1] - a * coordinates[0][0]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if y != a * x + b:
                return False

        return True


if __name__ == '__main__':
    print(checkStraightLine([[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]))
    print(checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
