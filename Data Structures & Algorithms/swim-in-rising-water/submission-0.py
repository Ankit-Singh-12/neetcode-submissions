class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        visit.add((0, 0))
        minheap = [(grid[0][0], 0, 0)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while minheap:
            max_elevation, r, c = heapq.heappop(minheap)
            if r == n - 1 and c == n - 1:
                return max_elevation
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(minheap, (max(grid[nr][nc], max_elevation), nr, nc))
        
        return -1
            