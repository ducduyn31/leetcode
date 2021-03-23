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


def bstFromPreorder(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder.pop(0))

    node_stack = [root]
    min_stack = [-sys.maxsize]
    max_stack = [sys.maxsize]

    while preorder:
        n = preorder[0]
        if min_stack[-1] < n < node_stack[-1].val:
            preorder.pop(0)
            max_stack.append(node_stack[-1].val)
            min_stack.append(min_stack[-1])
            node_stack.append(TreeNode(n))
            node_stack[-2].left = node_stack[-1]
        elif max_stack[-1] > n > node_stack[-1].val:
            preorder.pop(0)
            min_stack.append(node_stack[-1].val)
            max_stack.append(max_stack[-1])
            node_stack.append(TreeNode(n))
            node_stack[-2].right = node_stack[-1]
        else:
            min_stack.pop()
            max_stack.pop()
            node_stack.pop()

    return root


if __name__ == '__main__':
    print(bstFromPreorder([8, 5, 1, 7, 10, 12]))
