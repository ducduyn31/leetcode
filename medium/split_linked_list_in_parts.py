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

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        return self.get_chain_val() == other.get_chain_val()

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
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None] * k
        if not head:
            return result
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        part_size = size // k
        extra = size % k

        root = ListNode(0, head)
        current = root
        for i in range(k):
            current_size = part_size + (i < extra)
            last = current

            if not current.next:
                break

            result[i] = current.next
            for j in range(current_size):
                current = current.next

            last.next = None

        return result


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.split_list_to_parts = Solution().splitListToParts

    def test_1(self):
        input = ListNode.from_list([1, 2, 3])
        k = 5
        output = self.split_list_to_parts(input, k)
        self.assertEqual(output,
                         [ListNode.from_list([1]), ListNode.from_list([2]), ListNode.from_list([3]), None, None])

    def test_2(self):
        input = ListNode.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        k = 3
        output = self.split_list_to_parts(input, k)
        self.assertEqual(output, [ListNode.from_list([1, 2, 3, 4]), ListNode.from_list([5, 6, 7]),
                                  ListNode.from_list([8, 9, 10])])
