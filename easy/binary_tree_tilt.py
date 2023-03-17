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


def findTilt(root: TreeNode) -> int:
    if not root:
        return 0

    def sum_weight(root: TreeNode) -> (int, int):
        left_weight, right_weight = 0, 0
        left_tilt, right_tilt = 0, 0

        if root.left:
            left_weight, left_tilt = sum_weight(root.left)
        if root.right:
            right_weight, right_tilt = sum_weight(root.right)

        return left_weight + right_weight + root.val, abs(left_weight - right_weight) + left_tilt + right_tilt

    return sum_weight(root)[1]


if __name__ == '__main__':
    print(findTilt(TreeNode.from_list([1, 2, 3])))
    print(findTilt(TreeNode.from_list([4, 2, 9, 3, 5, None, 7])))
    print(findTilt(TreeNode.from_list([21, 7, 14, 1, 1, 2, 2, 3, 3])))
