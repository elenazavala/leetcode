class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board:
            return board
        
        
        # look for O's in the border
                
        
        visited = [[False for row in range(len(board[0]))]for col in range(len(board))]
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):                
                # check if this is the first or last row                
                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[i]) - 1:
                    # if there is an 'O' dfs through all 'O's and change visited array 
                    if board[i][j] == 'O':
                        self.dfs(i, j, board, visited)                    
                
                
        for i in range(len(board)):
            for j in range(len(board[i])):
                if visited[i][j] == False:
                    board[i][j] = 'X'
        return board
                
                    
        
        
    # turns all connected O's True in visited
    def dfs(self, i, j, board, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] == 'X' or visited[i][j] == True:
            return
                                                         
        visited[i][j] = True                                                
                                                         
                                                    
        
        self.dfs(i+1, j, board, visited)
        self.dfs(i-1, j, board, visited) 
        self.dfs(i, j+1, board, visited) 
        self.dfs(i, j-1, board, visited)
