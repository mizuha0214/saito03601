from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        k_count = 0

        for start in range(len(nums)):
            for end in range(start, len(nums)):
                subarray = nums[start:end+1]

                if sum(subarray) == k:
                    k_count += 1

        return k_count

