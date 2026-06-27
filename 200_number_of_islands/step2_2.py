from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark_island(r:int, c: int):
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                return

            if (r, c) in visited_grid:
                return

            if grid[r][c] == "0":
                return


            visited_grid.add((r, c))

            mark_island(r-1, c)
            mark_island(r+1, c)
            mark_island(r, c-1)
            mark_island(r, c+1)

        islands_count = 0
        visited_grid = set()

        num_rows = len(grid)
        num_cols = len(grid[0])

        for r in range(num_rows):
            for c in range(num_cols):
                if (r, c) in visited_grid:
                    continue
                if grid[r][c] == "1":
                    islands_count += 1
                    mark_island(r, c)

        return islands_count