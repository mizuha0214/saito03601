import heapq
from typing import List

class Solution:
    def count_frequency(self):
        frequency_dict = {}

        for num in self.nums:
            if num not in frequency_dict:
                frequency_dict[num] = 0
            frequency_dict[num] += 1

        frequency_tuple = [
            (-freq, num)
            for num, freq in frequency_dict.items()
        ]

        return frequency_tuple

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.nums = nums
        frequency_tuple = self.count_frequency()

        heapq.heapify(frequency_tuple)

        top_k_list = []
        for _ in range(k):
            most_frequent_num = heapq.heappop(frequency_tuple)
            top_k_list.append(most_frequent_num[1])

        return top_k_list

if __name__ == '__main__':
    nums = [1,1,1,1,5,5,3,3,3,4]
    k = 2
    result = Solution().topKFrequent(nums, 2)
    print(result)
