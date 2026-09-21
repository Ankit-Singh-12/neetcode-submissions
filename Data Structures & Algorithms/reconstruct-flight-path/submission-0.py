class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets = sorted(tickets)[::-1]
        for src, dest in tickets:
            graph[src].append(dest)
        
        res = []
        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs('JFK')
        return res[::-1]