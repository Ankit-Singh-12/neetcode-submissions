class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        currdp = [0] * (n + 1)
        dp = [0] * (n + 1)

        dp[-1] = currdp[-1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                currdp[c] = dp[c]

                if s[r] == t[c]:
                    currdp[c] += dp[c + 1]
                
            dp = currdp[:]
        
        return dp[0]