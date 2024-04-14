import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.next = next
        self.val = x

    def get_chain_val(self):
        if self.next is None:
            return str(self.val)

        return str(self.val) + ' - > ' + self.next.get_chain_val()

    def print(self):
        print(self.get_chain_val())

    def __str__(self):
        return self.get_chain_val()

    def concat(self, next_list: 'ListNode'):
        last = self
        while last.next:
            last = last.next

        last.next = next_list

        return self

    @staticmethod
    def from_list(nums: List[int]) -> 'ListNode':
        head = None
        current = None
        for i, n in enumerate(nums):
            if i == 0:
                head = ListNode(n)
                current = head
            else:
                next = ListNode(n)
                current.next = next
                current = next
        return head


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        index = 0

        current = root
        while index < left - 1:
            current = current.next
            index += 1

        start = last = current
        end = current = current.next

        while index < right:
            current.next, last, current = last, current, current.next
            index += 1

        start.next, end.next = last, current

        return root.next


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.reverse = Solution().reverseBetween

    def test_1(self):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        left = 2
        right = 4
        expected = ListNode.from_list([1, 4, 3, 2, 5])
        self.assertEqual(expected.get_chain_val(), self.reverse(head, left, right).get_chain_val())

    def test_2(self):
        head = ListNode.from_list([5])
        left = 1
        right = 1
        expected = ListNode.from_list([5])
        self.assertEqual(expected.get_chain_val(), self.reverse(head, left, right).get_chain_val())
