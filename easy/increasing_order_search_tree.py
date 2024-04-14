from typing import List, Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
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


def increasingBST(root: TreeNode) -> TreeNode:
    def straighten(root: TreeNode) -> List:
        left = straighten(root.left) if root.left else []
        right = straighten(root.right) if root.right else []

        return [*left, root, *right]

    nodes = straighten(root)

    for i in range(1, len(nodes)):
        nodes[i].left = None
        nodes[i - 1].right = nodes[i]

    return nodes[0]


if __name__ == '__main__':
    print(increasingBST(TreeNode.from_list([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])))
    print(increasingBST(TreeNode.from_list([5, 1, 7])))
