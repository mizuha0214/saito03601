class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            parent, lower_limit, upper_limit = stack.pop()
            parent_val = parent.val

            if not (lower_limit < parent_val < upper_limit):
                return False

            if parent.left:
                stack.append((parent.left, lower_limit, parent_val))

            if parent.right:
                stack.append((parent.right, parent_val, upper_limit))

        return True