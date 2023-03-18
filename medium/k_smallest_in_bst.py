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


def kthSmallest(root: TreeNode, k: int) -> int:

    def dfs(current_node: TreeNode, search_for: int) -> (int, TreeNode):
        if not current_node:
            return 0, None, False

        lcount, lnode, return_now = dfs(current_node.left, search_for)
        if return_now:
            return lcount, lnode, return_now
        count = lcount + 1

        if count == search_for:
            return k, current_node, True

        if count < k:
            rcount, rnode, return_now =  dfs(current_node.right, search_for - count)
            if return_now:
                return rcount, rnode, return_now
            return rcount + count, rnode, return_now

    return dfs(root, k)[1].val


if __name__ == '__main__':
    print(kthSmallest(TreeNode.from_list([3, 1, 4, None, 2]), 1))
    print(kthSmallest(TreeNode.from_list([5, 3, 6, 2, 4, None, None, 1]), 3))
