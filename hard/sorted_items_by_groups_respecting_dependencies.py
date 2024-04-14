import unittest
from collections import defaultdict
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # If an item belongs to zero group, assign it a unique group id.
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        # Sort all item regardless of group dependencies.
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        # Sort all groups regardless of item dependencies.
        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                # Each (prev -> curr) represents an edge in the item graph.
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                # If they belong to different groups, add an edge in the group graph.
                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

                    # Tologlogical sort nodes in graph, return [] if a cycle exists.

        def topologicalSort(graph, indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for neib in graph[cur]:
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        stack.append(neib)
            return visited if len(visited) == len(graph) else []

        item_order = topologicalSort(item_graph, item_indegree)
        group_order = topologicalSort(group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        # Items are sorted regardless of groups, we need to
        # differentiate them by the groups they belong to.
        ordered_groups = defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        # Concatenate sorted items in all sorted groups.
        # [group 1, group 2, ... ] -> [(item 1, item 2, ...), (item 1, item 2, ...), ...]
        answer = []
        for group_index in group_order:
            answer += ordered_groups[group_index]
        return answer


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sort_items = Solution().sortItems

    def test_sort_items_case_1(self):
        n = 8
        m = 2
        group = [-1, -1, 1, 0, 0, 1, 0, -1]
        before_items = [[], [6], [5], [6], [3, 6], [], [], []]
        expected = [6, 3, 4, 1, 5, 2, 0, 7]

        self.assertEqual(expected, self.sort_items(n, m, group, before_items))

    def test_sort_items_case_2(self):
        n = 8
        m = 2
        group = [-1, -1, 1, 0, 0, 1, 0, -1]
        before_items = [[], [6], [5], [6], [3], [], [4], []]
        expected = []

        self.assertEqual(expected, self.sort_items(n, m, group, before_items))
