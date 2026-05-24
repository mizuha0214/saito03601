import heapq
from typing import List


class Solution:
    def kSmallestPairs(
            self,
            nums1: List[int],
            nums2: List[int],
            k: int
    ) -> List[List[int]]:
        min_heap = []
        visited = set()
        result = []

        def _add_to_candidates(x, y):
            if x < len(nums1) and y < len(nums2) and (x, y) not in visited:
                heapq.heappush(
                    min_heap,
                    (
                        nums1[x] + nums2[y],
                        x,
                        y
                    )
                )
                visited.add((x, y))

        _add_to_candidates(0, 0)
        while len(result) < k:
            sum_current, current_i, current_j = heapq.heappop(min_heap)
            result.append([nums1[current_i], nums2[current_j]])

            _add_to_candidates(current_i + 1, current_j)
            _add_to_candidates(current_i, current_j + 1)

        return result
