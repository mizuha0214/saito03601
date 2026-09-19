# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        queue = deque()
        queue.append((root1, root2))

        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val

            # 左
            if node1.left is None:
                node1.left = node2.left
            elif node2.left is not None:
                queue.append((node1.left, node2.left))

            # 右
            if node1.right is None:
                node1.right = node2.right
            elif node2.right is not None:
                queue.append((node1.right, node2.right))

        return root1



