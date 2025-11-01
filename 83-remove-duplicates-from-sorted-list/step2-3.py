# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checking = head
        non_duplicate_end = head

        if head is None:
            return None

        while checking is not None:
            if checking.val != non_duplicate_end.val:
                non_duplicate_end.next = checking
                non_duplicate_end = checking
            checking = checking.next

        non_duplicate_end.next = None

        return head