class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        max_length = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    max_length[i] = max(max_length[i], max_length[j] + 1)

        return max(max_length)