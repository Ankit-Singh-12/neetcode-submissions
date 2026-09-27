class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q: 
            r, c = q.popleft()
            
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if not 0 <= nr < rows or not 0 <= nc < cols:
                    continue
                
                if grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))