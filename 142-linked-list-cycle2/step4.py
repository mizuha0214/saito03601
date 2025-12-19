# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #meetingが存在する＝循環が存在する
        meeting = self.find_meeting_node(head)
        if meeting is None:
            return None

        return self.find_cycle_start(head, meeting)

    def find_meeting_node(self, head: Optional[ListNode]):
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return fast

        return None

    def find_cycle_start(self, from_head: Optional[ListNode], from_meeting: Optional[ListNode]):
        while from_head is not from_meeting:
            from_head = from_head.next
            from_meeting = from_meeting.next

        return from_head







