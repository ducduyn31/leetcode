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

    def get_next_nth_node(self, n) -> 'ListNode':
        if n == 0:
            return self
        return self.next.get_next_nth_node(n - 1)

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


def deleteNode(node: ListNode):
    replace_node = node.next
    if replace_node:
        node.val = replace_node.val
        node.next = replace_node.next


if __name__ == '__main__':
    l = ListNode.from_list([4, 5, 1, 9])
    deleteNode(l.get_next_nth_node(1))
    print(l)
    l = ListNode.from_list([4, 5, 1, 9])
    deleteNode(l.get_next_nth_node(2))
    print(l)
    l = ListNode.from_list([1, 2, 3, 4])
    deleteNode(l.get_next_nth_node(2))
    print(l)
    l = ListNode.from_list([0, 1])
    deleteNode(l.get_next_nth_node(0))
    print(l)
    l = ListNode.from_list([-3, 5, -99])
    deleteNode(l.get_next_nth_node(0))
    print(l)
