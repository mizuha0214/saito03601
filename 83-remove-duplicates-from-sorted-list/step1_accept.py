# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = head
        seen_val = set()
        count = 0

        while curr_node is not None:
            if curr_node.val in seen_val:
                prev_node.next = curr_node.next
            else:
                seen_val.add(curr_node.val)
                if count != 0:
                    prev_node = prev_node.next

            curr_node = curr_node.next
            count += 1

        return head
