class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh, res = 0, 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while fresh > 0 and q:
            r, c, time = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if not 0 <= nr < rows or not 0 <= nc < cols or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                    continue
                
                grid[nr][nc] = 2
                fresh -= 1
                res = time + 1
                q.append((nr, nc, time + 1))
        

        return res if fresh == 0 else -1