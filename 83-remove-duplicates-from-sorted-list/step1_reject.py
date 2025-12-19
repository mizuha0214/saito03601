# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        visited_val = set()
        result = []

        while current_node is not None:
            if current_node.val not in visited_val:
                visited_val.add(current_node.val)
                result.append(current_node)
            current_node = current_node.next

        return result