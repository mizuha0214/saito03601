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

        while checking is not None:
            if checking.val == non_duplicate_end.val:
                non_duplicate_end.next = checking.next
            else:
                non_duplicate_end = checking
            checking = checking.next

        return head
