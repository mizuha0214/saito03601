# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        tail_node = dummy_node
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = 0
            if l1 is not None:
                digit1 = l1.val
            digit2 = 0
            if l2 is not None:
                digit2 = l2.val

            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            node = ListNode(digit)
            tail_node.next = node
            tail_node = node

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_node.next
