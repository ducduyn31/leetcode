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


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    def minNodeAndOther(l1: ListNode, l2: ListNode) -> (ListNode, ListNode):
        return (l1, l2) if l1.val <= l2.val else (l2, l1)

    def swap_node(l1: ListNode, l2: ListNode):
        l1.val, l2.val = l2.val, l1.val
        l1.next, l2.next = l2.next, l1.next

    min_node, max_node = minNodeAndOther(l1, l2)
    current_node = min_node

    while current_node and current_node.val <= max_node.val:
        if not current_node.next:
            current_node.next = max_node
            return min_node
        current_node = current_node.next

    if current_node:
        swap_node(current_node, max_node)

    mergeTwoLists(current_node, max_node)

    return min_node


if __name__ == '__main__':
    print(mergeTwoLists(ListNode.from_list([1, 2, 4]), ListNode.from_list([1, 3, 4])))
    print(mergeTwoLists(ListNode.from_list([]), ListNode.from_list([])))
    print(mergeTwoLists(ListNode.from_list([]), ListNode.from_list([0])))
