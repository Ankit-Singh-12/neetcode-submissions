class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS, lenP = len(s), len(p)
        cache = {}

        def dfs(indexS, indexP):
            if indexP == lenP:
                return indexS == lenS
            
            if (indexS, indexP) in cache:
                return cache[(indexS, indexP)]
            
            match = indexS < lenS and (s[indexS] == p[indexP] or p[indexP] == ".")

            if indexP + 1 < lenP and p[indexP + 1] == "*":
                cache[(indexS, indexP)] = dfs(indexS, indexP + 2) or (match and dfs(indexS + 1, indexP))
                return cache[(indexS, indexP)]
            
            if match:
                cache[(indexS, indexP)] = dfs(indexS + 1, indexP + 1)
                return cache[(indexS, indexP)]
            
            cache[(indexS, indexP)] = False
            return False


        return dfs(0 , 0)