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


def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    ans = defaultdict(list)

    Q = [(root, 0)]

    while Q:
        current, level = Q.pop(0)
        ans[level].append(current.val)
        if current.left:
            Q.append((current.left, level + 1))
        if current.right:
            Q.append((current.right, level + 1))

    return list(ans.values())


if __name__ == '__main__':
    print(levelOrder(TreeNode.from_list([3, 9, 20, None, None, 15, 7])))
