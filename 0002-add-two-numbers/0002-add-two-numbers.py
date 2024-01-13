# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        v = 0
        carry = 0
        tfin = []
        while (l1 is not None or l2 is not None or carry != 0):
            
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            v = digit1 + digit2 + carry
            if v >= 10:
                carry = 1
                v = v - 10
            else:
                carry = 0
            node = ListNode(v)
            tfin.append(node)
            if c != 0:
                tfin[c-1].next = tfin[c]

            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            c+=1

        return tfin[0]