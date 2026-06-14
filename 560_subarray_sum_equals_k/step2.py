from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = defaultdict(int)

        prefix_sum = 0
        count = 0

        prefix_sum_to_count[0] = 1

        for num in nums:
            prefix_sum += num

            count += prefix_sum_to_count[prefix_sum - k]

            prefix_sum_to_count[prefix_sum] += 1

        return count
