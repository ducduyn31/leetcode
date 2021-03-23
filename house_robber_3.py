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


def rob(root: TreeNode) -> int:
    if not root:
        return 0

    def dfs(root: TreeNode) -> (int, int):
        if not root.left and not root.right:
            return root.val, 0

        rob_left, rob_right = 0, 0
        skip_left, skip_right = 0, 0

        if root.left:
            rob_left, skip_left = dfs(root.left)
        if root.right:
            rob_right, skip_right = dfs(root.right)

        return max(rob_left + rob_right, skip_left + skip_right + root.val), rob_left + rob_right

    return dfs(root)[0]


if __name__ == '__main__':
    print(rob(TreeNode.from_list([3, 2, 3, None, 3, None, 1])))
    print(rob(TreeNode.from_list([3, 4, 5, 1, 3, None, 1])))
