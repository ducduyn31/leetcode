from typing import List


def validSquare(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    def dist_square(p1: List[int], p2: List[int]):
        return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

    p1p2 = dist_square(p1, p2)

    if p1p2 == 0:
        return False

    p1p3 = dist_square(p1, p3)
    p1p4 = dist_square(p1, p4)
    p2p3 = dist_square(p2, p3)
    p2p4 = dist_square(p2, p4)
    p3p4 = dist_square(p3, p4)

    return any([
        p1p2 == p3p4 == 2*p1p3 == 2*p1p4 == 2*p2p3 == 2*p2p4,
        p1p3 == p2p4 == 2*p1p2 == 2*p1p4 == 2*p2p3 == 2*p3p4,
        p1p4 == p2p3 == 2*p1p2 == 2*p1p3 == 2*p2p4 == 2*p3p4,
    ])


if __name__ == '__main__':
    print(validSquare([0, 0], [1, 1], [1, 0], [0, 1]))
    print(validSquare([0, 0], [5, 0], [5, 4], [0, 4]))
    print(validSquare([1, 1], [5, 3], [3, 5], [7, 7]))
    print(validSquare([0, 1], [1, 2], [0, 2], [0, 0]))
    print(validSquare([1, 1], [0, 1], [1, 2], [0, 0]))
