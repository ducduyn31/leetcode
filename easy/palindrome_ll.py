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


def isPalindrome(head: ListNode) -> bool:
    if not head.next:
        return True
    slow, fast = head, head
    reverse = None

    while fast and fast.next:
        fast, slow, reverse, reverse.next = fast.next.next, slow.next, slow, reverse

    if fast:
        slow = slow.next

    while slow:
        if reverse.val != slow.val:
            return False
        slow, reverse = slow.next, reverse.next

    return not reverse


if __name__ == '__main__':
    assert isPalindrome(ListNode.from_list([1])) is True
    assert isPalindrome(ListNode.from_list([1, 2])) is False
    assert isPalindrome(ListNode.from_list([1, 2, 1])) is True
    assert isPalindrome(ListNode.from_list([1, 2, 2, 1])) is True
