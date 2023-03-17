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


def closestNode(root: TreeNode, key: int) -> TreeNode:
    diff = 2147483648
    curr = root
    closest = 0

    while curr:
        if not curr.left:

            # updating diff if the current diff is
            # smaller than prev difference
            if diff > abs(curr.data - key):
                diff = abs(curr.data - key)
                closest = curr

            curr = curr.right
        else:

            # finding the inorder predecessor
            pre = curr.left
            while not pre.right and pre.right != curr:
                pre = pre.right

            if pre.right == None:
                pre.right = curr
                curr = curr.left

                # threaded link between curr and
            # its predecessor already exists
            else:
                pre.right = None

                # if a closer Node found, then update
                # the diff and set closest to current
                if diff > abs(curr.data - key):
                    diff = abs(curr.data - key)
                    closest = curr

                    # moving to the right child
                curr = curr.right

    return closest
