# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None:
            return None

        new_head, _ = self.reverseListHelper(head)
        return new_head

    def reverseListHelper(self, node: Optional[ListNode]):
        next_node = node.next

        if next_node is None:
            return node, node

        head, tail = self.reverseList(next_node)  # 自分より下を逆順にしてくれる。
        tail.next = node
        node.next = None
        tail = node

        return head, tail