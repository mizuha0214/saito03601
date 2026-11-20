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

            # 左の子が存在するなら追加
            if node.left:
                sum_left = node_sum + node.left.val
                stack.append((node.left, sum_left))
            # 右の子が存在するなら追加
            if node.right:
                sum_right = node_sum + node.right.val
                stack.append((node.right, sum_right))

        return False
