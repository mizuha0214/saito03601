# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        meeting = self.search_meeting(head)
        if meeting:
            cycle_start = self.get_cycle_start(head, meeting)
            return cycle_start
        else:
            return None

    def search_meeting(self, head: Optional[ListNode]):
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return fast

        return None

    def get_cycle_start(self, from_head: ListNode, from_meeting: ListNode):
        while from_head is not from_meeting:
            from_head = from_head.next
            from_meeting = from_meeting.next

        return from_head
