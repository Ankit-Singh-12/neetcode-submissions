class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        area = 0

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            local_area = 1
            for dx, dy in dirs:
                local_area += dfs(r + dx, c + dy)
            return local_area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    area = max(area, dfs(i, j))
        
        return area