import unittest
from typing import List


class TrieNode:
    def __init__(self, is_final=False):
        self.children = {}
        self.is_final = is_final


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_str(self, value: str):
        current_node = self.root
        for char in value:
            node = TrieNode()
            if char not in current_node.children:
                current_node.children[char] = node
            else:
                node = current_node.children[char]
            current_node = node

        current_node.is_final = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert_str(word)

        word_break = [False] * len(s)

        for break_point in range(len(s)):
            if break_point == 0 or word_break[break_point - 1]:
                current_node = trie.root

                for index in range(break_point, len(s)):
                    if s[index] not in current_node.children:
                        break

                    if current_node.children[s[index]].is_final:
                        word_break[index] = True

                    current_node = current_node.children[s[index]]

        return word_break[-1]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.wordBreak = Solution().wordBreak

    def tearDown(self) -> None:
        self.wordBreak = None

    def test_word_break_should_return_true_given_leet_code(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.wordBreak(s, wordDict))

    def test_word_break_should_return_true_given_apple_pen(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.wordBreak(s, wordDict))

    def test_word_break_should_return_false_given_cats_and_dogs(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.wordBreak(s, wordDict))

    def test_word_break_should_return_true_given_cats_and_dogs(self):
        s = "catsandog"
        wordDict = ["ca", "ts", "an", "do", "catsando", "andog"]
        self.assertTrue(self.wordBreak(s, wordDict))

    def test_word_break_should_return_false_given_aaaaaaa(self):
        s = "aaaaaaa"
        wordDict = ["aaaa", "aa"]
        self.assertFalse(self.wordBreak(s, wordDict))

    def test_word_break_should_return_true_given_bb(self):
        s = "bb"
        wordDict = ["a", "b", "bbb", "bbbb"]
        self.assertTrue(self.wordBreak(s, wordDict))

    def test_word_break_should_return_false_given_long_str(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
        self.assertFalse(self.wordBreak(s, wordDict))
