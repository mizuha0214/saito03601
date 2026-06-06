from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_nums = set()

        num1_set = set(nums1) # O(len(nums1))
        for num2 in nums2:  # O(len(nums2))
            if num2 in num1_set:  # O(1)
                intersection_nums.add(num2)

        return list(intersection_nums)

