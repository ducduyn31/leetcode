import collections
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


# def verticalTraversal(root: TreeNode) -> List[List[int]]:
#     if not root:
#         return []
#
#     S = [(0, root)]
#     M = {}
#
#     while S:
#         y, node = S.pop()
#         if y not in M:
#             M[y] = [node.val]
#         else:
#             M[y].append(node.val)
#
#         if node.left:
#             S.append((y - 1, node.left))
#         if node.right:
#             S.append((y + 1, node.right))
#
#     return list(map(lambda x: x[1], sorted(M.items())))

def verticalTraversal(root: TreeNode) -> List[List[int]]:
    seen = collections.defaultdict(
        lambda: collections.defaultdict(list))

    def dfs(node, x=0, y=0):
        if node:
            seen[x][y].append(node)
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)

    dfs(root)
    ans = []

    for x in sorted(seen):
        report = []
        for y in sorted(seen[x]):
            report.extend(sorted(node.val for node in seen[x][y]))
        ans.append(report)

    return ans


if __name__ == '__main__':
    print(verticalTraversal(TreeNode.from_list([0, 2, 1, 3, None, None, None, 4, 5, None, 7, 6, None, 10, 8, 11, 9])))
    print(verticalTraversal(TreeNode.from_list([3, 9, 20, None, None, 15, 7])))
    print(verticalTraversal(TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])))
    print(verticalTraversal(TreeNode.from_list([1])))
