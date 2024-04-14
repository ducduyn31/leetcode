import unittest
from typing import List


class NestedInteger:
    def __init__(self, value):
        self.value = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.value, int)

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if self.isInteger():
            return self.value
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        if self.isInteger():
            return None
        else:
            return self.value

    def __repr__(self):
        return self.value


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.nested_list = self.recursive_get(nestedList)
        self.peek = None

    def recursive_get(self, nl: List[NestedInteger]):
        for ni in nl:
            if ni.isInteger():
                yield ni.getInteger()
            else:
                yield from self.recursive_get(ni.getList())

    def next(self) -> int:
        if self.hasNext():
            temp = self.peek
            self.peek = None
            return temp
        return None

    def hasNext(self) -> bool:
        if self.peek is not None:
            return True
        try:
            self.peek = next(self.nested_list)
            return True
        except:
            return False


class NestedIteratorTest(unittest.TestCase):
    def test_1(self):
        nested_list = [NestedInteger([1, 1]), NestedInteger(2), NestedInteger([1, 1])]
        nested_iterator = NestedIterator(nested_list)
        self.assertEqual(1, nested_iterator.next())
        self.assertEqual(1, nested_iterator.next())
        self.assertEqual(2, nested_iterator.next())
        self.assertEqual(1, nested_iterator.next())
        self.assertEqual(1, nested_iterator.next())
        self.assertEqual(False, nested_iterator.hasNext())

    def test_2(self):
        nested_list = [NestedInteger(1), NestedInteger([4, [6]])]
        nested_iterator = NestedIterator(nested_list)
        self.assertEqual(1, nested_iterator.next())
        self.assertEqual(4, nested_iterator.next())
        self.assertEqual(6, nested_iterator.next())
        self.assertEqual(False, nested_iterator.hasNext())
