from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_nums = set()

        nums1_set = set(nums1)
        for num2 in nums2:
            if num2 in nums1_set:
                intersection_nums.add(num2)

        return list(intersection_nums)

