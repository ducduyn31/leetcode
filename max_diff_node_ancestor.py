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


def maxAncestorDiff(root: TreeNode) -> int:
    def dfs(root: TreeNode, max_ancestor: int, min_ancestor) -> int:
        left, right = 0, 0
        if root.left:
            left = dfs(root.left, max(max_ancestor, root.left.val), min(min_ancestor, root.left.val))
        if root.right:
            right = dfs(root.right, max(max_ancestor, root.right.val), min(min_ancestor, root.right.val))
        return max(left, right, abs(root.val - max_ancestor), abs(root.val - min_ancestor))

    return dfs(root, root.val, root.val)


if __name__ == '__main__':
    print(maxAncestorDiff(TreeNode.from_list([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])))
    print(maxAncestorDiff(TreeNode.from_list([1, None, 2, None, 0, 3])))
