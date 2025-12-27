# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        carry = 0

        while l1 or l2 or carry != 0:
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                total += l2.val
                l2 = l2.next

            digit = total % 10
            carry = total // 10

            node = ListNode(digit)

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
        return head