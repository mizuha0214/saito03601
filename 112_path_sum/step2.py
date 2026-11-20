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

        stack = []
        # node, nodeまでのvalの累積値
        stack.append((root, root.val))

        while stack:
            node, node_sum = stack.pop()

            # leafなら、ここでtargetSumと比較
            if node.left is None and node.right is None:
                if node_sum == targetSum:
                    return True

            # 左右の子がいるならstackに追加
            for child in (node.left, node.right):
                if child is not None:
                    child_sum = node_sum + child.val
                    stack.append((child, child_sum))

        return False
