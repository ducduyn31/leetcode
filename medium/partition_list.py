import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.next = None
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first_big = last_big = ListNode(0)
        first_small = last_small = ListNode(0)

        current = head
        while current:
            if current.val < x:
                last_small.next = current
                last_small = last_small.next
            else:
                last_big.next = current
                last_big = last_big.next

            current = current.next

        last_small.next, last_big.next = first_big.next, None

        return first_small.next


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.partition_list = Solution().partition

    def test_partition_list_should_work_for_x_3_and_len_6(self):
        head = ListNode.from_list([1, 4, 3, 2, 5, 2])
        expected = ListNode.from_list([1, 2, 2, 4, 3, 5])
        self.assertEqual(expected.get_chain_val(), self.partition_list(head, 3).get_chain_val())

    def test_partition_list_should_work_for_x_2_and_len_2(self):
        head = ListNode.from_list([2, 1])
        expected = ListNode.from_list([1, 2])
        self.assertEqual(expected.get_chain_val(), self.partition_list(head, 2).get_chain_val())

    def test_partition_list_should_work_for_x_3_and_len_5(self):
        head = ListNode.from_list([4, 3, 2, 5, 2])
        expected = ListNode.from_list([2, 2, 4, 3, 5])
        self.assertEqual(expected.get_chain_val(), self.partition_list(head, 3).get_chain_val())
