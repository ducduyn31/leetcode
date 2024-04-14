from collections import defaultdict
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


def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    levels = defaultdict(set)
    Q = [(root, 0, 0)]
    while Q:
        node, level, index = Q.pop()
        if level > 0:
            if (node.val, 2 ** level - index - 1) not in levels[level]:
                levels[level].add((node.val, index))
            else:
                levels[level].discard((node.val, 2 ** level - index - 1))
        if node.left:
            Q.append((node.left, level + 1, 2 * index))
        if node.right:
            Q.append((node.right, level + 1, 2 * index + 1))

    return not any(levels.values())



if __name__ == '__main__':
    print(isSymmetric(TreeNode.from_list([1, 2, 2, 3, 4, 4, 3])))
    print(isSymmetric(TreeNode.from_list([1, 2, 2, None, 3, None, 3])))
