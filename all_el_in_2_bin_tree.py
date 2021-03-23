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


def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:
    results = []

    def dfs(root: TreeNode):
        if not root:
            return
        S = [root]
        while S:
            current = S.pop()
            results.append(current.val)
            if current.right:
                S.append(current.right)
            if current.left:
                S.append(current.left)

    dfs(root1)
    dfs(root2)

    return sorted(results)


if __name__ == '__main__':
    print(getAllElements(TreeNode.from_list([2, 1, 4]), TreeNode.from_list([1, 0, 3])))
    print(getAllElements(TreeNode.from_list([0, -10, 10]), TreeNode.from_list([5, 1, 7, 0, 2])))
    print(getAllElements(TreeNode.from_list([]), TreeNode.from_list([5, 1, 7, 0, 2])))
    print(getAllElements(TreeNode.from_list([0, -10, 10]), TreeNode.from_list([])))
    print(getAllElements(TreeNode.from_list([1, None, 8]), TreeNode.from_list([8, 1])))
