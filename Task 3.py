#https://leetcode.com/problems/game-of-life/?difficulty=MEDIUM

#0 (dead), stays dead → 0
#0 (dead), becomes live → 2
#1 (live), stays live → 1
#1 (live), dies → -1

class Solution(object):
    def gameOfLife(self, board):
        
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] == 1 or board[ni][nj] == -1:
                            live_neighbors += 1
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2 

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
