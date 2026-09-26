class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        temp = [0] * (n + 1)

        for src, dest in trust:
            temp[src] -= 1
            temp[dest] += 1
        
        for i in range(n + 1):
            if temp[i] == n - 1:
                return i
        
        return -1