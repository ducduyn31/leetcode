import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._last_index = 0
        self._set = {}
        self._rev = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self._set:
            self._set[val] = self._last_index
            self._rev[self._last_index] = val
            self._last_index += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self._set:
            del self._rev[self._set[val]]
            del self._set[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randint(0, self._last_index)

        while i not in self._rev:
            i = random.randint(0, self._last_index)

        return self._rev[i]


if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())
