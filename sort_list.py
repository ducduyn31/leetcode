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

    def __eq__(self, other):
        if not isinstance(other, ListNode) and other is not None:
            return False
        if self.val is None and other is None:
            return True
        return self.get_chain_val() == other.get_chain_val()


class LinkedList:
    def __init__(self, nums: List[int]):
        self.first = self.from_list(nums)

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

    def __str__(self):
        l = []

        current = self.first

        while current:
            l.append(current.val)
            current = current.next

        return str(l)


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    def append_node(current_node: ListNode, next_node: Optional[ListNode]):
        if not current_node:
            return next_node
        current_node.next = next_node
        return next_node

    def concat_sorted_list(left: Optional[ListNode], right: Optional[ListNode]):
        if not left:
            return right
        if not right:
            return left
        mid = left
        while mid.next:
            mid = mid.next
        mid.next = right
        return left

    pivot = head
    current = head.next
    right_head = right_tail = None
    left_head = left_tail = None
    pivot.next = None

    while current:
        if current.val <= pivot.val:
            left_head = left_head if left_head else current
            left_tail = append_node(left_tail, current)
        else:
            right_head = right_head if right_head else current
            right_tail = append_node(right_tail, current)

        current = current.next
        if not current:
            left_tail = append_node(left_tail, None)
            right_tail = append_node(right_tail, None)

    return concat_sorted_list(sortList(left_head), concat_sorted_list(pivot, sortList(right_head)))


if __name__ == '__main__':
    assert sortList(
        LinkedList.from_list([25, 44, 25, 46, 36, 46, 10, 9, 3, 30, 2, 41, 3, 26, 20])) == LinkedList.from_list(
        [2, 3, 3, 9, 10, 20, 25, 25, 26, 30, 36, 41, 44, 46, 46]
    )
    assert sortList(LinkedList.from_list([4, 2, 1, 3])) == LinkedList.from_list([1, 2, 3, 4])
    assert sortList(LinkedList.from_list([-1, 5, 3, 4, 0])) == LinkedList.from_list([-1, 0, 3, 4, 5])
    assert sortList(LinkedList.from_list([])) == LinkedList.from_list([])
