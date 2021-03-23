import sys
from typing import List, Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

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


def isValidBST(root: TreeNode) -> bool:
    def validBSTRecursive(root: TreeNode, max_val, min_val) -> bool:
        if not root:
            return True

        if min_val >= root.val or root.val >= max_val:
            return False

        if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
            return False

        return all([validBSTRecursive(root.left, root.val, min_val), validBSTRecursive(root.right, max_val, root.val)])

    return validBSTRecursive(root, sys.maxsize, -sys.maxsize)


if __name__ == '__main__':
    print(isValidBST(TreeNode.from_list([1, 1])))
    print(isValidBST(TreeNode.from_list([2, 1, 3])))
    print(isValidBST(TreeNode.from_list([5, 1, 4, None, None, 3, 6])))
    print(isValidBST(TreeNode.from_list([10, 5, 15, None, None, 6, 20])))
