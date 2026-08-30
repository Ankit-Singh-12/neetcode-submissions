class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        direction = -1
        i = 0

        for c in s:
            rows[i].append(c)
            if i == 0 or i == numRows - 1:
                direction *= -1
            i += direction
        
        return "".join("".join(row) for row in rows)