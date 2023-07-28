import unittest
from typing import List, Union


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val

    @staticmethod
    def from_list(nodes: List[int], index=0) -> Union['TreeNode', None]:
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
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        parents_map = {}

        def parse_tree(node: TreeNode, parent):
            parents_map[node.val] = parent

            if node.left:
                parse_tree(node.left, node)
            if node.right:
                parse_tree(node.right, node)

        parse_tree(root, None)

        to_visit = set(map(lambda node: node.val, nodes))

        def dfs(node: TreeNode):
            if not to_visit or not node or not node.val:
                return None

            ret = None

            if node.val in to_visit:
                to_visit.remove(node.val)
                ret = node

            left = None
            right = None

            if node.left:
                left = dfs(node.left)

            if node.right:
                right = dfs(node.right)

            if ret:
                return ret

            if left and right:
                return node
            if not left and not right:
                return None
            return left or right

        return dfs(root)


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lowest_common_ancestor = Solution().lowestCommonAncestor

    def test_lowest_common_ancestor_should_return_2_given_4_7(self):
        root = TreeNode.from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        nodes = [TreeNode(4), TreeNode(7)]
        self.assertEqual(TreeNode(2), self.lowest_common_ancestor(root, nodes))

    def test_lowest_common_ancestor_should_return_1_given_1(self):
        root = TreeNode.from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        nodes = [TreeNode(1)]
        self.assertEqual(TreeNode(1), self.lowest_common_ancestor(root, nodes))

    def test_lowest_common_ancestor_should_return_5_given_7_6_2_4(self):
        root = TreeNode.from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        nodes = [TreeNode(7), TreeNode(6), TreeNode(2), TreeNode(4)]
        self.assertEqual(TreeNode(5), self.lowest_common_ancestor(root, nodes))

    def test_lowest_common_ancestor_should_return_5481(self):
        root = TreeNode.from_list(
            [12795, 1982, None, 3798, None, 430, None, 5481, None, 15224, None, 12970, None, 18652, None, 5137, None,
             13230, None, 8433, None, 19989, None, 6921])
        nodes = [TreeNode(5481), TreeNode(13230), TreeNode(18652)]
        self.assertEqual(TreeNode(5481), self.lowest_common_ancestor(root, nodes))
