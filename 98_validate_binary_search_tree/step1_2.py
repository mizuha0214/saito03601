# これは正しくない。step1_3が正しい。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return False

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            parent, lower_limit, upper_limit = stack.pop()
            parent_val = parent.val

            if parent.left:
                if parent_val < upper_limit:
                    upper_limit = parent_val
                    if not (lower_limit < parent.left.val < upper_limit):
                        return False
                    stack.append((parent.left, lower_limit, upper_limit))
            if parent.right:
                if parent_val > lower_limit:
                    lower_limit = parent_val
                    if not (lower_limit < parent.right.val < upper_limit):
                        return False
                    stack.append((parent.right, lower_limit, upper_limit))

        return True
