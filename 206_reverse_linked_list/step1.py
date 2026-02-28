# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head

        while node is not None:
            stack.append(node)
            node = node.next

        dummy_node = ListNode(0)
        result_tail = dummy_node
        while stack:
            node = stack.pop()
            node.next = None
            result_tail.next = node
            result_tail = node

        return dummy_node.next
