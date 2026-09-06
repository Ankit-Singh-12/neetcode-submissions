class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def dfs(i, j, seen):
            seen[i][j] = True

            for dx, dy in dirs:
                nr, nc = i + dx, j + dy

                if 0 <= nr < m and 0 <= nc < n and not seen[nr][nc] and heights[i][j] <= heights[nr][nc]:
                    dfs(nr, nc, seen) 
        
        for r in range(m):
            dfs(r, 0, pacific)
        for c in range(n):
            dfs(0, c, pacific)

        for r in range(m):
            dfs(r, n - 1, atlantic)
        for c in range(n):
            dfs(m - 1, c, atlantic)

        res = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])
        return res        