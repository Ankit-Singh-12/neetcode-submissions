class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visit[node] = True

            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for i in range(n):
            if not visit[i]:
                bfs(i)
                res += 1
        
        return res