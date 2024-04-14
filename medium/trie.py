from collections import defaultdict
from typing import List


def clazz_runner(steps: List[str], parameters: List[List], out):
    obj = globals()[steps[0]](*parameters[0])
    steps.pop(0)
    parameters.pop(0)

    for f, a in zip(steps, parameters):
        ret_value = getattr(obj, f)(*a)
        if ret_value and out:
            out(ret_value)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        nested_dd = lambda: defaultdict(nested_dd)
        self._dict = nested_dd()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        last_dict = self._dict
        for c in word:
            last_dict = last_dict[c]
        last_dict['.'] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        Q = [self._dict]

        def is_word(the_word: str, current_dict) -> bool:
            last_dict = current_dict
            for c in the_word:
                if c not in last_dict:
                    return False
                last_dict = last_dict[c]
            return '.' in last_dict

        while Q:
            current_dict = Q.pop()
            if current_dict and word[0] in current_dict and is_word(word, current_dict):
                return True

        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        last_dict = self._dict
        for c in prefix:
            if c not in last_dict:
                return False
            last_dict = last_dict[c]
        return True


if __name__ == '__main__':
    clazz_runner(["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
                 [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]], print)
