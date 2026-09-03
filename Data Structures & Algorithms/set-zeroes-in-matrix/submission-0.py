class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rowzero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        rowzero = True
                    else:
                        matrix[r][0] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0
        
        if rowzero:
            for c in range(n):
                matrix[0][c] = 0
        