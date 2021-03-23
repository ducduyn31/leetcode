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


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:

    curr_A, curr_B = headA, headB

    while curr_A != curr_B:
        curr_A = curr_A.next if curr_A else headB
        curr_B = curr_B.next if curr_B else headA

    return curr_A


if __name__ == '__main__':
    intersect = ListNode.from_list([8, 4, 5])
    print(getIntersectionNode(ListNode.from_list([4, 1]).concat(intersect), ListNode.from_list([5, 6, 1]).concat(intersect)))
    intersect = ListNode.from_list([2, 4])
    print(getIntersectionNode(ListNode.from_list([1, 9, 1]).concat(intersect), ListNode.from_list([3]).concat(intersect)))
    intersect = ListNode.from_list([])
    print(getIntersectionNode(ListNode.from_list([2, 6, 4]).concat(intersect), ListNode.from_list([1, 5]).concat(intersect)))
