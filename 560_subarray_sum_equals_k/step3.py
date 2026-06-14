from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = defaultdict(int)

        # 累積和 0 が最初に 1 回出現している
        prefix_sum_to_count[0] = 1

        current_prefix_sum = 0
        result = 0

        for num in nums:
            current_prefix_sum += num

            target_prefix_sum = current_prefix_sum - k
            result += prefix_sum_to_count[target_prefix_sum]

            prefix_sum_to_count[current_prefix_sum] += 1

        return result