import unittest
from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.char = None
        self.children = defaultdict(TrieNode)
        self.is_final = False
        self.length = 0

    def __getitem__(self, item) -> 'TrieNode':
        return self.children[item]

    def __setitem__(self, key, value):
        self.children[key] = value

    def __contains__(self, item):
        return item in self.children

    def __repr__(self):
        if not self.char:
            return ''
        return self.char


class Solution:

    @staticmethod
    def construct_trie(dictionary: List[str]) -> TrieNode:
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                node[c].char = c
                node[c].length = node.length + 1
                node = node[c]

            node.is_final = True

        return root

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = self.construct_trie(dictionary)
        dp = [0]
        candidates = []
        for ch in s:
            next_candidates = []
            if ch in root:
                next_candidates.append(root[ch])

            while candidates:
                candidate = candidates.pop()
                if ch in candidate:
                    next_candidates.append(candidate[ch])

            this_min = dp[-1] + 1
            for candidate in next_candidates:
                if candidate.is_final:
                    this_min = min(dp[-candidate.length], this_min)
            dp.append(this_min)

            candidates = next_candidates

        return dp[-1]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.min_extra_char = Solution().minExtraChar

    def test_min_extra_char_should_return_1_given_leetscode(self):
        self.assertEqual(1, self.min_extra_char('leetscode', ['leet', 'code', 'leetcode']))

    def test_min_extra_char_should_return_3_given_sayhelloworld(self):
        self.assertEqual(3, self.min_extra_char('sayhelloworld', ['hello', 'world']))

    def test_min_extra_char_should_return_3_given_sayhelloworlddddd(self):
        self.assertEqual(7, self.min_extra_char('sayhelloworlddddd', ['hello', 'world']))

    def test_min_extra_char_should_return_7_given_dwmodizxvvbosxxw(self):
        self.assertEqual(7, self.min_extra_char('dwmodizxvvbosxxw',
                                                ["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e",
                                                 "wmo", "cehy", "tskz", "ds", "kzbu"]))
