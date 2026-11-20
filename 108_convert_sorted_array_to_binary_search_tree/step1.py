# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # 真ん中を取る。
        # 真ん中を基準に左と右に分ける。
        if not nums:
            return None

        middle = len(nums)//2
        root_value = nums[middle]
        left = nums[:middle]
        right = nums[middle+1:]

        root = TreeNode(root_value)
        left_middle = self.sortedArrayToBST(left)
        right_middle = self.sortedArrayToBST(right)
        root.left = left_middle
        root.right = right_middle

        return root
