class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque([i, j] for i in range(rows) for j in range(cols) if grid[i][j] == 0)
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        while q:
            r, c = q.popleft()

            for dx, dy in dirs:
                nr, nc = r + dx, c + dy

                if min(nr, nc) < 0 or nr >= rows or nc >= cols:
                    continue
                if grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append([nr, nc])






