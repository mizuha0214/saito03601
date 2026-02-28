# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListHelper(head, previous):
            if head is None:
                return previous
            next_node = head.next
            head.next = previous
            return reverseListHelper(next_node, head)

        return reverseListHelper(head, None)