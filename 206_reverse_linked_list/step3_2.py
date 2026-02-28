#step2_2で解く。
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        found_nodes = []
        node_in_original = head
        while node_in_original is not None:
            found_nodes.append(node_in_original)
            node_in_original = node_in_original.next

        reversed_head = found_nodes.pop()
        node_in_reversed = reversed_head
        while found_nodes:
            next_node = found_nodes.pop()
            node_in_reversed.next = next_node
            node_in_reversed = next_node
            node_in_reversed.next = None # 古いループを断ち切る

        return reversed_head
