from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited_grid = set()

        num_row = len(grid)
        num_col = len(grid[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        for start_row in range(num_row):
            for start_col in range(num_col):
                if (start_row, start_col) in visited_grid:
                    continue

                if grid[start_row][start_col] == 0:
                    continue

                current_area = 1
                stack = [(start_row, start_col)]
                visited_grid.add((start_row, start_col))

                while stack:
                    row, col = stack.pop()

                    for change_row, change_col in directions:
                        neighbor_row = row + change_row
                        neighbor_col = col + change_col

                        if neighbor_row < 0 or neighbor_row >= num_row or neighbor_col < 0 or neighbor_col >= num_col:
                            continue

                        if (neighbor_row, neighbor_col) in visited_grid:
                            continue

                        if grid[neighbor_row][neighbor_col] == 0:
                            continue

                        current_area += 1
                        stack.append((neighbor_row, neighbor_col))
                        visited_grid.add((neighbor_row, neighbor_col))

                max_area = max(max_area, current_area)

        return max_area

