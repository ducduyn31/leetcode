# Definition for singly-linked list.
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


class Solution:
    def addTwoNodes(self, l1: ListNode, l2: ListNode, c: int):

        a = 0
        b = 0

        if l1 is not None:
            a = l1.val
        if l2 is not None:
            b = l2.val

        r = a + b + c

        c = 0

        if r >= 10:
            r -= 10
            c = 1

        return ListNode(r), c

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res, c = self.addTwoNodes(l1, l2, 0)

        temp = res
        A = l1.next
        B = l2.next

        while c is not 0 or A is not None or B is not None:

            R, c = self.addTwoNodes(A, B, c)

            temp.next = R
            temp = temp.next

            if A is not None:
                A = A.next

            if B is not None:
                B = B.next

        return res


if __name__ == '__main__':
    s = Solution()
    ll1 = ListNode(9)
    ll1.next = ListNode(9)
    ll1.next.next = ListNode(9)

    ll2 = ListNode(9)
    ll2.next = ListNode(9)
    ll2.next.next = ListNode(9)
    ll2.next.next.next = ListNode(9)

    print(s.addTwoNumbers(ll1, ll2).get_chain_val())
