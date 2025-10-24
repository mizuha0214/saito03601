from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        current = head
        list_nodes = set()
        while current is not None:
            if current in list_nodes:
                return True

            list_nodes.add(current)
            current = current.next

        return False


