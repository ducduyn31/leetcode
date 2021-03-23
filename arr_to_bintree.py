import math
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


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    def midToNode(left, right) -> Union[TreeNode, None]:
        if left > right:
            return None
        mid = math.ceil((left + right) / 2)

        return TreeNode(nums[mid], midToNode(left, mid - 1), midToNode(mid + 1, right))

    return midToNode(0, len(nums) - 1)


if __name__ == '__main__':
    print(sortedArrayToBST([-10, -3, 0, 5, 9]))
