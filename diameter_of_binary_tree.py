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


def depth(root: TreeNode, priorMax: List[int]):
    if not root:
        return 0

    leftHeight = depth(root.left, priorMax)
    rightHeight = depth(root.right, priorMax)

    priorMax[0] = max(priorMax[0], leftHeight + rightHeight)

    return 1 + max(leftHeight, rightHeight)


def diameterOfBinaryTree(root: TreeNode) -> int:
    if not root:
        return 0
    result = [-1]
    depth(root, result)

    return result[0]


if __name__ == '__main__':
    root = TreeNode.from_list([1, 2, 3, 4, 5])
    print(diameterOfBinaryTree(root))

    root = TreeNode.from_list([])
    print(diameterOfBinaryTree(root))

    root = TreeNode.from_list(
        [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1,
         -4, None, None, None, -2])
    print(diameterOfBinaryTree(root))
