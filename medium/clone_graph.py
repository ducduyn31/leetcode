import unittest
from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @staticmethod
    def from_adj_list(adj_list: List[List[int]]):
        if len(adj_list) == 0:
            return None

        nodes = {}

        for i in range(len(adj_list)):
            nodes[i + 1] = Node(val=i + 1)

        for i, adj in enumerate(adj_list):
            for j in adj:
                nodes[i + 1].neighbors.append(nodes[j])
        return nodes[1]

    def __eq__(self, other: 'Node'):
        return self.val == other.val and all(
            node.val == self.neighbors[i].val for i, node in enumerate(other.neighbors))

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if len(node.neighbors) == 0:
            return Node(node.val)

        node_map = {}
        adj_list = {}
        visited = {node.val}
        q = [node]

        while len(q) > 0:
            current = q.pop()

            if current.val in node_map:
                continue

            node_map[current.val] = Node(val=current.val)
            adj_list[current.val] = map(lambda n: n.val, current.neighbors)

            for n in current.neighbors:
                if n.val in visited:
                    continue
                q.append(n)
                visited.add(n.val)

        for node_val, neighbors in adj_list.items():
            node_map[node_val].neighbors.extend(map(lambda n_id: node_map[n_id], neighbors))

        return node_map[1]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cloneGraphs = Solution().cloneGraph

    def test_clone_graph_should_clone_a_circular_graph(self):
        graph = Node.from_adj_list([[2, 4], [1, 3], [2, 4], [1, 3]])
        cloned = self.cloneGraphs(graph)
        self.assertEqual(cloned, graph)

    def test_clone_graph_should_clone_a_graph_with_one_node(self):
        graph = Node.from_adj_list([[]])
        cloned = self.cloneGraphs(graph)
        self.assertEqual(cloned, graph)

    def test_clone_graph_should_clone_an_empty_graph(self):
        graph = Node.from_adj_list([])
        cloned = self.cloneGraphs(graph)
        self.assertEqual(cloned, graph)
