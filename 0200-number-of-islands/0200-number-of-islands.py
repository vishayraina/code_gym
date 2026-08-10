class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            grid[i][j] = 0
            if i > 0:
                if grid[i-1][j] == "1":
                    dfs(i-1,j)
            if i < m-1:
                if grid[i+1][j] == "1":
                    dfs(i+1,j)
            if j > 0:
                if grid[i][j-1] == "1":
                    dfs(i,j-1)
            if j < n-1:
                if grid[i][j+1] == "1":
                    dfs(i,j+1)
            return 
        def print_grid():
            for i in range(m):
                for j in range(n):
                    print(grid[i][j], end=" ")
                print()
            print()
                    
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res 