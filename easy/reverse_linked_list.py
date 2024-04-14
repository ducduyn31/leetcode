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


def reverseList(head: ListNode) -> ListNode:
    past = None
    current = head
    next = current.next if current else None

    while current:
        current.next = past
        past = current
        current = next
        next = next.next if next else None

    return past


if __name__ == '__main__':
    # print(reverseList(ListNode.from_list([1, 2, 3, 4, 5])))
    print(reverseList(ListNode.from_list([])))
