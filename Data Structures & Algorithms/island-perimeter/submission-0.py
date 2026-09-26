class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    res += 4
                    if r and grid[r - 1][c]:
                        res -= 2
                    if c and grid[r][c - 1]:
                        res -= 2
        
        return res