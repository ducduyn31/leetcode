import heapq
import unittest
from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return self.name


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        nodes = {}

        for start, end in tickets:
            if start not in nodes:
                start_node = Node(start)
                nodes[start] = start_node
            else:
                start_node = nodes[start]

            if end not in nodes:
                end_node = Node(end)
                nodes[end] = end_node
            else:
                end_node = nodes[end]

            heapq.heappush(start_node.children, end_node)

        result = []

        def dfs(name: str):
            while nodes[name].children:
                next_node = heapq.heappop(nodes[name].children)
                dfs(next_node.name)

            result.append(name)

        dfs('JFK')

        return result[::-1]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.find_itinerary = Solution().findItinerary

    def test_find_itinerary_1(self):
        self.assertEqual(["JFK", "MUC", "LHR", "SFO", "SJC"], self.find_itinerary(
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        ))

    def test_find_itinerary_2(self):
        self.assertEqual(["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"], self.find_itinerary(
            [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        ))

    def test_find_itinerary_3(self):
        self.assertEqual(["JFK", "NRT", "JFK", "KUL"], self.find_itinerary(
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        ))

    def test_find_itinerary_4(self):
        self.assertEqual(
            ["JFK", "ATL", "PHX", "LAX", "JFK", "ORD", "PHL", "ATL"], self.find_itinerary(
                [["JFK", "ATL"], ["ORD", "PHL"], ["JFK", "ORD"], ["PHX", "LAX"], ["LAX", "JFK"], ["PHL", "ATL"],
                 ["ATL", "PHX"]]
            ))

    def test_find_itinerary_5(self):
        self.assertEqual(
            ["JFK", "ANU", "EZE", "AXA", "TIA", "ANU", "JFK", "TIA", "ANU", "TIA", "JFK"], self.find_itinerary(
                [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"],
                 ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]
            ))

    def test_find_itinerary_6(self):
        self.assertEqual(
            ["JFK", "AAA", "JFK", "CCC", "JFK", "BBB"], self.find_itinerary(
                [["JFK", "AAA"], ["AAA", "JFK"], ["JFK", "BBB"], ["JFK", "CCC"], ["CCC", "JFK"]]
            ))
