# Definition for singly-linked list.
from typing import List, Union, Any, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other


class LinkedList:
    def __init__(self, nums: List[int]):
        self.first = self.from_list(nums)

    def from_list(self, nums: List[int]) -> ListNode:
        first = ListNode(nums[0])
        current = first
        n = len(nums)

        for _ in range(n - 1):
            current.next = ListNode(nums[1])
            nums.pop(0)
            current = current.next

        return first

    def __str__(self):
        l = []

        current = self.first

        while current:
            l.append(current.val)
            current = current.next

        return str(l)


def middleNode(head: ListNode) -> ListNode:
    slow = fast = head

    def move(point: ListNode, step: int):
        result = point
        for _ in range(step):
            if result.next:
                result = result.next
            else:
                return None
        return result

    while fast and fast.next:
        fast = move(fast, 2)
        slow = move(slow, 1)

    return slow


if __name__ == '__main__':
    assert middleNode(LinkedList([1, 2, 3, 4, 5]).first) == 3
    assert middleNode(LinkedList([1, 2, 3, 4, 5, 6]).first) == 4
