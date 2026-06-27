from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_island_area(r: int, c: int):
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                return 0

            if (r, c) in visited_grid:
                return 0

            if grid[r][c] == 0:
                return 0

            visited_grid.add((r, c))

            return(
                1
                + get_island_area(r - 1, c)
                + get_island_area(r + 1, c)
                + get_island_area(r, c - 1)
                + get_island_area(r, c + 1)
            )

        max_area = 0
        visited_grid = set()

        num_rows = len(grid)
        num_cols = len(grid[0])

        for r in range(num_rows):
            for c in range(num_cols):
                if (r, c) in visited_grid:
                    continue

                if grid[r][c] == 0:
                    continue

                area = get_island_area(r, c)
                max_area = max(max_area, area)

        return max_area