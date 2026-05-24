import heapq
from typing import List

from pycparser.c_ast import While


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

        def _add_to_candidates_if_necessary(x, y):
            if (
                    x < len(nums1)
                    and y < len(nums2)
                    and (x, y) not in visited
            ):
                heapq.heappush(
                    min_heap,
                    (
                        nums1[x] + nums2[y],
                        x,
                        y
                    )
                )
                visited.add((x, y))

        # min_heapに最初の要素を追加。行=0, 列=0
        _add_to_candidates_if_necessary(0, 0)

        while len(result) < k:
            # min_heapの最小値を取り出し、resultに追加
            current_sum, current_i, current_j = heapq.heappop(min_heap)
            result.append([nums1[current_i], nums2[current_j]])

            # 今の最小値の次に小さい候補をmin_heapに追加
            # 右
            _add_to_candidates_if_necessary(current_i+1, current_j)
            # 下
            _add_to_candidates_if_necessary(current_i, current_j+1)

        return result






