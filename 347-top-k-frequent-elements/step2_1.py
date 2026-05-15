import heapq
from typing import List

class Solution:
    def _build_frequency_pairs(self, nums):
        frequency_by_num = {}

        for num in nums:
            if num not in frequency_by_num:
                frequency_by_num[num] = 0
            frequency_by_num[num] += 1

        frequency_num_pairs = [
            (-freq, num)
            for num, freq in frequency_by_num.items()
        ]

        return frequency_num_pairs

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_num_pairs = self._build_frequency_pairs(nums)

        heapq.heapify(frequency_num_pairs)

        top_k_list = []
        for _ in range(k):
            most_frequent_num = heapq.heappop(frequency_num_pairs)
            top_k_list.append(most_frequent_num[1])

        return top_k_list

if __name__ == '__main__':
    nums = [1,1,1,1,5,5,3,3,3,4]
    k = 2
    result = Solution().topKFrequent(nums, 2)
    print(result)
