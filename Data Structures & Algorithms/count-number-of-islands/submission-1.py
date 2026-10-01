class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        res = 0

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dx, dy in dirs:
                dfs(r + dx, c + dy)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res