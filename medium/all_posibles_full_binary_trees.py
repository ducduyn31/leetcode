import unittest
from typing import List, Union, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    @staticmethod
    def from_list(nodes: List[int], index=0) -> Union["TreeNode", None]:
        if not nodes:
            return None
        r = TreeNode(nodes[0])
        nodes.pop(0)
        nodes_queue = [r]

        while len(nodes_queue) > 0:
            if len(nodes) > 0:
                left = nodes.pop(0)
                if left is not None:
                    nodes_queue[0].left = TreeNode(left)
                    nodes_queue.append(nodes_queue[0].left)
            if len(nodes) > 0:
                right = nodes.pop(0)
                if right is not None:
                    nodes_queue[0].right = TreeNode(right)
                    nodes_queue.append(nodes_queue[0].right)

            nodes_queue.pop(0)
        return r


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        dp = []
        children = self.allPossibleFBT(n - 2)








class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.all_possible_fbt = Solution().allPossibleFBT

    def assertFullBST(
        self, expected_trees: List[TreeNode], actual_trees: List[TreeNode]
    ):
        self.assertCountEqual(expected_trees, actual_trees)

    def test_should_return_all_possible_combination_given_7(self):
        expected = [
            TreeNode.from_list([0, 0, 0, None, None, 0, 0, None, None, 0, 0]),
            TreeNode.from_list([0, 0, 0, None, None, 0, 0, 0, 0]),
            TreeNode.from_list([0, 0, 0, 0, 0, 0, 0]),
            TreeNode.from_list([0, 0, 0, 0, 0, None, None, None, None, 0, 0]),
            TreeNode.from_list([0, 0, 0, 0, 0, None, None, 0, 0]),
        ]

        self.assertFullBST(expected, self.all_possible_fbt(7))

    def test_should_return_all_possible_combination_given_3(self):
        expected = [
            TreeNode.from_list([0, 0, 0]),
        ]

        self.assertCountEqual(expected, self.all_possible_fbt(3))
