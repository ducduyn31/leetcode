import math
import unittest
from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log_height = n.bit_length() + 1
        self.up = [parent]

        for _ in range(1, self.log_height):
            temp = [-1] * n
            for node_id in range(n):
                if self.up[-1][node_id] == -1:
                    continue
                temp[node_id] = self.up[-1][self.up[-1][node_id]]
            self.up.append(temp)

    def getKthAncestor(self, node: int, k: int) -> int:
        if 1 << self.log_height < k:
            return -1

        for log_k in range(self.log_height - 1, - 1, -1):
            if node == -1:
                break
            if k >= (1 << log_k):
                node = self.up[log_k][node]
                k -= 1 << log_k

        return node


class TreeAncestorTest(unittest.TestCase):

    def test_1(self):
        tree = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
        self.assertEqual(1, tree.getKthAncestor(3, 1))
        self.assertEqual(0, tree.getKthAncestor(5, 2))
        self.assertEqual(-1, tree.getKthAncestor(6, 3))

    def test_2(self):
        tree = TreeAncestor(5, [-1, 0, 0, 0, 3])
        self.assertEqual(-1, tree.getKthAncestor(1, 5))
        self.assertEqual(-1, tree.getKthAncestor(3, 2))
        self.assertEqual(-1, tree.getKthAncestor(0, 1))
        self.assertEqual(0, tree.getKthAncestor(3, 1))
        self.assertEqual(-1, tree.getKthAncestor(3, 5))

    def test_3(self):
        tree = TreeAncestor(5, [-1, 0, 0, 1, 2])
        self.assertEqual(-1, tree.getKthAncestor(3, 5))
        self.assertEqual(0, tree.getKthAncestor(3, 2))
        self.assertEqual(-1, tree.getKthAncestor(2, 2))
        self.assertEqual(-1, tree.getKthAncestor(0, 2))
        self.assertEqual(0, tree.getKthAncestor(2, 1))

    def test_4(self):
        tree = TreeAncestor(4, [-1, 2, 3, 0])
        self.assertEqual(-1, tree.getKthAncestor(2, 3))
        self.assertEqual(0, tree.getKthAncestor(2, 2))
        self.assertEqual(3, tree.getKthAncestor(2, 1))

    def test_5(self):
        tree = TreeAncestor(6, [-1, 2, 3, 4, 5, 0])
        self.assertEqual(5, tree.getKthAncestor(1, 4))
