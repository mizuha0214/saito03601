# nodeまでの累計値をstackに入れていく。
from numpy.ma.core import not_equal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        # (node, そのnodeまでのvalの累積値)
        stack = [(root, root.val)]

        while stack:
            node, node_sum = stack.pop()

            if node.left is None and node.right is None:
                if node_sum == targetSum:
                    return True

            if node.left:
                left_sum = node_sum + node.left.val
                stack.append((node.left, left_sum))
            if node.right:
                right_sum = node_sum + node.right.val
                stack.append((node.right, right_sum))

        return False


