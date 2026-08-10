class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            area += dfs(i-1, j)
            area += dfs(i+1, j)
            area += dfs(i, j-1) 
            area += dfs(i, j+1)
            return area
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    print(i,j, area)
                    max_area = max(area, max_area)
        return max_area