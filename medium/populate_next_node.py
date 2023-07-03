from typing import List, Union


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def print_next(self) -> List[Union[int, str]]:
        nexts = [self.val]
        if self.next:
            nexts.extend(self.next.print_next())
        else:
            nexts.append('#')
            if self.left:
                nexts.extend(self.left.print_next())
            elif self.right:
                nexts.extend(self.right.print_next())

        return nexts

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    @staticmethod
    def from_list(nodes: List[int], index=0) -> Union['Node', None]:
        if not nodes:
            return None
        r = Node(nodes[0])
        nodes.pop(0)
        nodes_queue = [r]

        while len(nodes_queue) > 0:
            if len(nodes) > 0:
                left = nodes.pop(0)
                if left is not None:
                    nodes_queue[0].left = Node(left)
                    nodes_queue.append(nodes_queue[0].left)
            if len(nodes) > 0:
                right = nodes.pop(0)
                if right is not None:
                    nodes_queue[0].right = Node(right)
                    nodes_queue.append(nodes_queue[0].right)

            nodes_queue.pop(0)
        return r


def connect(root: Node) -> Node:
    if not root:
        return root

    def bfs(root: Node):
        Q = [(root, 0)]
        last_node, last_level = None, -1
        while Q:
            current, level = Q.pop(0)
            if last_node and last_level == level:
                last_node.next = current
                last_node = current
            else:
                last_node = current
                last_level = level

            if current.left:
                Q.append((current.left, level + 1))
            if current.right:
                Q.append((current.right, level + 1))

    bfs(root)
    return root


if __name__ == '__main__':
    print(connect(Node.from_list([1, 2, 3, 4, 5, 6, 7])).print_next())
