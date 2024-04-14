import unittest
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return f"{self.val} -> {self.next} | {self.random.val if self.random else None}"

    def __str__(self):
        return f"{self.val} -> {self.next} | {self.random.val if self.random else None}"

    @staticmethod
    def from_tuple_list(l: list):
        head, random_node_id = l[0]
        head_node = Node(head)
        current_node = head_node
        node_list = [head_node]
        for i in range(1, len(l)):
            node = Node(l[i][0])
            node_list.append(node)
            current_node.next = node
            current_node = node

        current_node = head_node
        for i in range(len(l)):
            random_node_id = l[i][1]
            current_node.random = node_list[random_node_id] if random_node_id is not None else None
            current_node = current_node.next

        return head_node


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        root = Node(0, head)

        while head:
            head.next = Node(head.val, head.next, head.random)
            head = head.next.next

        current = root.next.next
        while current:
            current.random = current.random.next if current.random else None
            current = current.next.next if current.next else None

        current = root.next.next
        while current:
            current.next = current.next.next if current.next else None
            current = current.next

        return root.next.next


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.copy_random_list = Solution().copyRandomList

    def test_copy_random_list_for_5_nodes(self):
        head = Node.from_tuple_list([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
        expected = Node.from_tuple_list([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
        self.assertEqual(str(expected), str(self.copy_random_list(head)))

    def test_copy_random_list_for_2_nodes(self):
        head = Node.from_tuple_list([(1, 1), (2, 1)])
        expected = Node.from_tuple_list([(1, 1), (2, 1)])
        self.assertEqual(str(expected), str(self.copy_random_list(head)))

    def test_copy_random_list_for_3_nodes(self):
        head = Node.from_tuple_list([(3, None), (3, 0), (3, None)])
        expected = Node.from_tuple_list([(3, None), (3, 0), (3, None)])
        self.assertEqual(str(expected), str(self.copy_random_list(head)))
