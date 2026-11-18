class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = [False] * n
        res = 0

        def dfs(city):
            visit[city] = True
            for j in range(n):
                if isConnected[city][j] == 1 and not visit[j]:
                    dfs(j)

        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        
        return res