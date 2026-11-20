# Definition for a binary tree node.
from sqlalchemy.log import rootlogger


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if nums is None:
            return

        root = TreeNode(0)

        stack = [(root, 0, len(nums)-1)]
        while stack:
            node, left, right = stack.pop()

            middle = (left+right) // 2
            node.val = nums[middle]

            if left < middle:
                node.left = TreeNode(0)
                stack.append((node.left, left, middle-1))

            if middle < right:
                node.right = TreeNode(0)
                stack.append((node.right, middle+1, right))

        return root