from typing import List


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


def oddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    odd_head = odd_tail = head
    even_head = even_tail = head.next

    while odd_tail.next and even_tail.next:
        if even_tail.next:
            odd_tail.next = odd_tail.next.next

        if odd_tail.next:
            even_tail.next = even_tail.next.next

        odd_tail = odd_tail.next
        even_tail = even_tail.next

    odd_tail.next = even_head

    return odd_head


if __name__ == '__main__':
    assert oddEvenList(LinkedList.from_list([])) is None
    assert oddEvenList(LinkedList.from_list([1, 2, 3, 4, 5, 6, 7, 8])) == LinkedList.from_list([1, 3, 5, 7, 2, 4, 6, 8])
    assert oddEvenList(LinkedList.from_list([1])) == LinkedList.from_list([1])
    assert oddEvenList(LinkedList.from_list([1, 2, 3, 4, 5])) == LinkedList.from_list([1, 3, 5, 2, 4])
    assert oddEvenList(LinkedList.from_list([2, 1, 3, 5, 6, 4, 7])) == LinkedList.from_list([2, 3, 6, 7, 1, 5, 4])
