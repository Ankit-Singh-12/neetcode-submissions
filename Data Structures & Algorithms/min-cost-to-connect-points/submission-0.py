class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [10000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextnode = -1

            for i in range(n):
                if visit[i]:
                    continue
                
                curdist = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))

                dist[i] = min(dist[i], curdist)

                if nextnode == -1 or dist[nextnode] > dist[i]:
                    nextnode = i
            
            node = nextnode
            res += dist[nextnode]
            edges += 1
        
        return res
            
