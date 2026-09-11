# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        next_layer = [(root, 1)]

        while next_layer:
            node, depth = next_layer.pop(0)

            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                next_layer.append((node.left, depth+1))

            if node.right is not None:
                next_layer.append((node.right, depth+1))
