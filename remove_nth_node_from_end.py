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
        return self.get_chain_val()

    def __repr__(self):
        return str(self.val)


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head

    nth_node = dummy
    curr_node = dummy

    for i in range(n):
        curr_node = curr_node.next

    while curr_node.next:
        curr_node = curr_node.next
        nth_node = nth_node.next

    nth_node.next = nth_node.next.next

    return dummy.next


if __name__ == '__main__':
    print(removeNthFromEnd(ListNode.from_list([1, 2, 3, 4, 5]), 2))
    print(removeNthFromEnd(ListNode.from_list([1]), 1))
