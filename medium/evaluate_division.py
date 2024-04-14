import unittest
from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equations_graph = defaultdict(dict)

        for i, [a, b] in enumerate(equations):
            equations_graph[a][b] = values[i]
            equations_graph[b][a] = 1 / values[i]

        def dfs(start: str, end: str, path=None):
            if path is None:
                path = set()
            path.add(start)
            next_nodes = equations_graph[start]
            if end in next_nodes:
                return next_nodes[end]

            for next_node in next_nodes:
                if next_node in path:
                    continue

                next_value = dfs(next_node, end, path)

                if next_value == -1.0:
                    continue

                return equations_graph[start][next_node] * next_value

            return -1.0

        return [dfs(c, d) for [c, d] in queries]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calcEquation = Solution().calcEquation

    def test_calc_equation_1(self):
        result = self.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                   queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
        self.assertEqual([6.00000, 0.50000, -1.00000, 1.00000, -1.00000], result)

    def test_calc_equation_2(self):
        result = self.calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                                   queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
        self.assertEqual([3.75000, 0.40000, 5.00000, 0.20000], result)

    def test_calc_equation_3(self):
        result = self.calcEquation(equations=[["a", "b"]], values=[0.5],
                                   queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
        self.assertEqual([0.50000, 2.00000, -1.00000, -1.00000], result)
