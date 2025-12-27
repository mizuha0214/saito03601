# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None      # 結果リストの先頭
        tail = None      # 今の末尾
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            node = ListNode(digit)

            if head is None:
                # 最初の1回だけ
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head
