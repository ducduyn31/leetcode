from typing import List


class SegmentTreeNode:

    def __init__(self, start: int, end: int, tree: 'SegmentTree'):
        self.range = (start, end)
        self.parent_tree = tree
        self.range_value = None
        self.value = {}
        self.left = None
        self.right = None

        if start == end:
            self._sync()

        self.left = SegmentTreeNode(start, (start + end) // 2, tree)
        self.right = SegmentTreeNode((start + end) // 2 + 1, end, tree)
        self._sync()

    def _sync(self):
        if self.range[0] == self.range[1]:
            current_value = self.parent_tree.array[self.range[0]]
            if self.range_value is not None:
                current_value = self.range_value
            self.value = sum([current_value])
        else:
            result = sum([self.left.value, self.right.value])
            if self.range_value is not None:
                bound_length = self.range[1] - self.range[0] + 1
                result = self.range_value * bound_length
            self.value = result

    def query(self, start: int, end: int):
        if end < self.range[0] or start > self.range[1]:
            return None

        if start <= self.range[0] and self.range[1] <= end:
            return self.value
        self._push()

        left_res = self.left.query(start, end) if self.left else None
        right_res = self.right.query(start, end) if self.right else None

        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return sum([left_res, right_res])

    def _push(self):
        if self.range_value is None:
            return
        if self.left:
            self.left.range_value = self.range_value
            self.right.range_value = self.range_value
            self.left._sync()
            self.right._sync()
            self.range_value = None


class SegmentTree:
    def __int__(self, arr: List[int]):
        self.array = arr
        self.root = SegmentTreeNode(0, len(arr) - 1, self)

    def query(self, start, end):
        return self.root.query(start, end)


def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    pass


if __name__ == '__main__':
    print(getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
