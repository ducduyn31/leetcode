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


def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    Q = [root]
    r = []
    while Q:
        current = Q.pop(0)

        if not current:
            continue

        smaller, larger = current.left, current.right

        if L <= current.val <= R:
            r.append(current.val)

        if L < current.val:
            Q.append(smaller)
        if current.val < R:
            Q.append(larger)

    return sum(r)


if __name__ == '__main__':
    # print(rangeSumBST(TreeNode.from_list([10, 5, 15, 3, 7, None, 18]), 7, 15))
    # print(rangeSumBST(TreeNode.from_list([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10))
    print(rangeSumBST(TreeNode.from_list(
        [100, 50, 150, 24, 76, 126, 176, 12, 38, 64, 88, 114, 138, 164, 188, 6, 18, 32, 44, 58, 70, 82, 94, 108, 120,
         132,
         144, 158, 170, 182, 194, 2, 10, 16, 22, 28, 36, 42, 48, 54, 62, 68, 74, 80, 86, 92, 98, 104, 112, 118, 124,
         130,
         136, 142, 148, 154, 162, 168, 174, 180, 186, 192, 198, 0, 4, 8, None, 14, None, 20, None, 26, 30, 34, None, 40,
         None, 46, None, 52, 56, 60, None, 66, None, 72, None, 78, None, 84, None, 90, None, 96, None, 102, 106, 110,
         None,
         116, None, 122, None, 128, None, 134, None, 140, None, 146, None, 152, 156, 160, None, 166, None, 172, None,
         178,
         None, 184, None, 190, None, 196]), 170, 178))
