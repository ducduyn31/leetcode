class BinaryMatrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._count = 0

    def get_count(self):
        return self._count

    def get(self, x: int, y: int) -> int:
        if self._count == 1000:
            raise RuntimeError('Exceed allowed get')
        self._count += 1
        return self._matrix[x][y]

    def dimensions(self) -> list:
        return [len(self._matrix), len(self._matrix[0])]


def leftMostColumnWithOne(binaryMatrix: BinaryMatrix) -> int:
    [max_row, max_col] = binaryMatrix.dimensions()
    left_most = max_col

    for r in range(max_row):
        left, right = 0, max_col - 1
        first_one = max_col

        while left <= right:
            mid = (left + right) // 2

            n = binaryMatrix.get(r, mid)

            if n == 1:
                right = mid - 1
                first_one = mid
            else:
                left = mid + 1

        left_most = min(first_one, left_most)

    return left_most if left_most != max_col else -1


if __name__ == '__main__':
    print(leftMostColumnWithOne(BinaryMatrix([[0, 0], [1, 1]])))
    print(leftMostColumnWithOne(BinaryMatrix([[0, 0], [0, 1]])))
    print(leftMostColumnWithOne(BinaryMatrix([[0, 0], [0, 0]])))
    print(leftMostColumnWithOne(BinaryMatrix([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])))
