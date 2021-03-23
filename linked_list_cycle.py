from typing import List


class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x
        self.loop_start = False

    def get_chain_val(self):
        if self.loop_start:
            Q = [str(self.val)]
            current = self.next
            while not current.loop_start:
                Q.append(str(current.val))
                current = current.next

            return '( ' + ' - > '.join(Q) + ' )'

        if self.next is None:
            return str(self.val)

        return str(self.val) + ' - > ' + self.next.get_chain_val()

    def print(self):
        print(self.get_chain_val())

    def __str__(self):
        return self.get_chain_val()

    @staticmethod
    def from_list(nums: List[int], pos: int = -1) -> 'ListNode':
        head = None
        current = None
        start_loop = None
        for i, n in enumerate(nums):
            if i == 0:
                head = ListNode(n)
                current = head
            else:
                next = ListNode(n)
                current.next = next
                current = next
            if i == pos:
                start_loop = current
                start_loop.loop_start = True
        current.next = start_loop
        return head


def hasCycle(head: ListNode) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow == fast:
            return True

    return False


if __name__ == '__main__':
    l = ListNode.from_list([3, 2, 0, -4], 1)
    print(hasCycle(l))
    l = ListNode.from_list([1, 2], 0)
    print(hasCycle(l))
    l = ListNode.from_list([1], -1)
    print(hasCycle(l))
