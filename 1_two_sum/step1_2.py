from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for index, num in enumerate(nums):
            search_num = target - num

            if search_num in num_to_index:
                return [num_to_index[search_num], index]

            num_to_index[num] = index

