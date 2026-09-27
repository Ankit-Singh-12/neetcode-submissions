class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        area = 0

        def bfs(i, j):
            q = deque([(i, j)])
            local_area = 1
            grid[i][j] = 0

            while q:
                r, c = q.popleft()
            
                for dx, dy in dirs:
                    nr, nc = dx + r, dy + c
                    if not 0 <= nr < rows or not 0 <= nc < cols or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    local_area += 1
                    q.append((nr, nc))
            return local_area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    area = max(area, bfs(i, j))
        
        return area