from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r:int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if (r, c) in visited_grid:
                return

            if grid[r][c] == "0":
                return


            visited_grid.add((r, c))

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        island_count = 0
        visited_grid = set()

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited_grid:
                    island_count += 1
                    dfs(r, c)

        return island_count