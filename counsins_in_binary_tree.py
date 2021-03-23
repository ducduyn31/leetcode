from typing import List, Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

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


def isCousins(root: TreeNode, x: int, y: int) -> bool:
    if not root:
        return False

    def bfs(r: TreeNode) -> bool:
        S = [(r, 0, 0, 0)]
        found = (-1, -1)

        while S:
            curr, level, j, root = S.pop(0)

            if (curr.val == x or curr.val == y) and found[0] == -1:
                found = (level, root)
                continue

            if curr.val == x or curr.val == y:
                if level == found[0] and root != found[1]:
                    return True
                else:
                    return False

            if curr.left:
                S.append((curr.left, level + 1, 2 * j + 1, j))
            if curr.right:
                S.append((curr.right, level + 1, 2 * j + 2, j))

        return False

    return bfs(root)


if __name__ == '__main__':
    print(isCousins(TreeNode.from_list([1, 2, 3, 4]), 4, 3))
    print(isCousins(TreeNode.from_list([1, 2, 3, None, 4, None, 5]), 5, 4))
    print(isCousins(TreeNode.from_list([1, 2, 3, None, 4]), 2, 3))
