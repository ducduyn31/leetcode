import unittest
from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        visited = set()

        left_set, right_set = set(leftChild), set(rightChild)
        root = -1

        for i in range(n):
            if i not in left_set and i not in right_set:
                root = i
                break
        if root == -1:
            return False

        stack = [root]

        while stack:
            node = stack.pop()
            visited.add(node)

            left, right = leftChild[node], rightChild[node]

            if left != -1:
                if left in visited:
                    return False
                stack.append(left)

            if right != -1:
                if right in visited:
                    return False
                stack.append(right)

        return len(visited) == n


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.validate_binary_tree_nodes = Solution().validateBinaryTreeNodes

    def test_1(self):
        self.assertTrue(
            self.validate_binary_tree_nodes(4, [1, -1, 3, -1], [2, -1, -1, -1])
        )

    def test_2(self):
        self.assertFalse(
            self.validate_binary_tree_nodes(4, [1, -1, 3, -1], [2, 3, -1, -1])
        )

    def test_3(self):
        self.assertFalse(self.validate_binary_tree_nodes(2, [1, 0], [-1, -1]))

    def test_4(self):
        self.assertTrue(
            self.validate_binary_tree_nodes(4, [3, -1, 1, -1], [-1, -1, 0, -1])
        )

    def test_5(self):
        self.assertFalse(
            self.validate_binary_tree_nodes(
                6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]
            )
        )
