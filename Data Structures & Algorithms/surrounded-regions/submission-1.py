class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols or board[r][c] != "O":
                return
            
            board[r][c] = '*'

            for dx, dy in dirs:
                dfs(r + dx, c + dy)
        
        for i in range(rows):
            for j in range(cols):
                if i * j == 0 or i == rows - 1 or j == cols - 1:
                    dfs(i, j)
    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
