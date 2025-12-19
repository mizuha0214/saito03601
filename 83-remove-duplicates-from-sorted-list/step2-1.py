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

        while curr_node is not None:
            next_node = curr_node.next
            if curr_node.val in seen_val:
                prev_node.next = next_node
            else:
                seen_val.add(curr_node.val)
                prev_node = curr_node

            curr_node = next_node

        return head
