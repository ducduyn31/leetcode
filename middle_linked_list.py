# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


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
    count = 0

    current = head
    index = {}

    while current:
        index[count] = current
        count += 1
        current = current.next

    return index[count // 2]


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5]
    print(middleNode(LinkedList(input).first))
    input = [1, 2, 3, 4, 5, 6]
    print(middleNode(LinkedList(input).first))
