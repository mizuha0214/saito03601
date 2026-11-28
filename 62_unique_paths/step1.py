class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_counts = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                path_counts[i][j] = path_counts[i-1][j] + path_counts[i][j-1]

        return path_counts[m-1][n-1]