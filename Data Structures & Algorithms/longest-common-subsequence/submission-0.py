class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + dp[j - 1]
                else:
                    curr[j] = max(curr[j - 1], dp[j])
            dp, curr = curr, [0] * (n + 1)

        return dp[-1]