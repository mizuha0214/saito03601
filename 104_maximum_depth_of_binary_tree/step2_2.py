# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]
        depth = 0

        while stack:
            node, current_depth = stack.pop()
            depth = max(current_depth, depth)

            if node.left is not None:
                stack.append((node.left, current_depth + 1))
            if node.right is not None:
                stack.append((node.right, current_depth + 1))

        return depth

