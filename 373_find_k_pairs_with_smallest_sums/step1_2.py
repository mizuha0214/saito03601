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

        # 最初のheap要素,visited要素を入れる。
        heapq.heappush(min_heap, ( nums1[0] + nums2[0], 0, 0) )
        visited.add((0,0))

        result = []
        while True:
            if len(result) == k:
                break

            # 今の最小ペアをheappopで求める。
            current_sum, current_i, current_j = heapq.heappop(min_heap)
            result.append( (nums1[current_i], nums2[current_j]) )

            # currentの1行先の要素を追加（currentの次に小さい候補）
            if current_i+1 < len(nums1) and (current_i+1, current_j) not in visited:
                heapq.heappush(
                    min_heap,
                    (
                        nums1[current_i + 1] + nums2[current_j],
                        current_i + 1,
                        current_j
                    )
                )
                visited.add(( current_i+1, current_j ))

            # currentの1行下の要素を追加（currentの次に小さい候補）
            if current_j+1 < len(nums2) and (current_i, current_j+1) not in visited:
                heapq.heappush(
                    min_heap,
                    (
                        nums1[current_i] + nums2[current_j + 1],
                        current_i,
                        current_j + 1
                    )
                )
                visited.add((current_i, current_j + 1))

        return result



