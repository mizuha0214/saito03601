from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_1, num1 in enumerate(nums):
            for i_2, num2 in enumerate(nums):
                if i_1 == i_2:
                    continue

                num_sum = num1 + num2
                if num_sum == target:
                    return [i_1, i_2]

