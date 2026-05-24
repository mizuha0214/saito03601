import heapq
from typing import List


class Solution:
    def _make_sum(self, nums1, nums2):
        sum_num_pairs = [ ]
        for num1 in nums1:
            for num2 in nums2:
                pair_sum = num1 + num2
                sum_num_pairs.append((-pair_sum, (num1, num2)))
        return sum_num_pairs

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 1. num1とnum2の要素和の配列を作る。[(-4, (1, 3)), (-5, (1,4))]
        # 2. heappushでheapを作る。
        # ただし、要素がk個以上になったら、heappop。ただし、heapの要素にはマイナス符号を付けておく。
        # [(-4, (1, 3)), (-4, (2, 2))]
        sum_infos = self._make_sum(nums1, nums2)

        max_heap = []
        for sum_info in sum_infos:
            heapq.heappush(max_heap, sum_info)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        k_num_pairs = []
        for pair_sum, num_pair in max_heap:
            k_num_pairs.append(num_pair)

        return k_num_pairs

if __name__ == '__main__':
    nums1 = [1, 3, 6, 7, 9]
    nums2 = [2, 3, 4, 5, 8]
    k = 4
    result = Solution().kSmallestPairs(nums1, nums2, k)
    print(result)



