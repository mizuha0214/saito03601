class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sums = nums.copy()

        for i in range(1, len(nums)):
            max_sums[i] = max(nums[i], max_sums[i-1] + nums[i])

        return max(max_sums)

