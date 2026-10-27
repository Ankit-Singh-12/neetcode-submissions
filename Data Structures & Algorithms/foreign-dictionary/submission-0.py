class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        state = {c: 0 for c in adj}
        result = []

        def dfs(c):
            state[c] = 1
            for nei in adj[c]:
                if state[nei] == 1:
                    return False
                
                if state[nei] == 0:
                    if not dfs(nei):
                        return False
            state[c] = 2
            result.append(c)
            return True
        
        for c in adj:
            if state[c] == 0:
                if not dfs(c):
                    return ""

        return "".join(reversed(result))
        
