class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}

        for i in range(len(s)):
            lastindex[s[i]] = i
        
        res = []
        start = 0
        end = 0

        for i, c in enumerate(s):
            end = max(end, lastindex[c])

            if i == end:
                res.append(end - start + 1)
                start = end + 1
        
        return res