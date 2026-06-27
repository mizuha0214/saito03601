from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited_grid = set()
        max_area = 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        for start_row in range(num_rows):
            for start_col in range(num_cols):
                if (start_row, start_col) in visited_grid:
                    continue

                if grid[start_row][start_col] == 0:
                    continue

                current_area = 0

                stack = [(start_row, start_col)]
                visited_grid.add((start_row, start_col))

                while stack:
                    row, col = stack.pop()
                    current_area += 1

                    # 上下左右を追加
                    for row_change, col_change in directions:
                        neighbor_row = row + row_change
                        neighbor_col = col + col_change

                        if neighbor_row < 0 or neighbor_row >= num_rows or neighbor_col < 0 or neighbor_col >= num_cols:
                            continue

                        if (neighbor_row, neighbor_col) in visited_grid:
                            continue

                        if grid[neighbor_row][neighbor_col] == 0:
                            continue

                        visited_grid.add((neighbor_row, neighbor_col))
                        stack.append((neighbor_row, neighbor_col))

                max_area = max(max_area, current_area)


        return max_area