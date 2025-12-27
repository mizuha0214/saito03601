# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            digit1 = 0
            if l1:
                digit1 = l1.val
            digit2 = 0
            if l2:
                digit2 = l2.val

            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10

            node = ListNode(digit)
            tail.next = node
            tail = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
