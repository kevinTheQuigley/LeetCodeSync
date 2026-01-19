class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_col=len(board[0])
        len_row=len(board)

        def dfs(board,position,word):
            
            char = word[0]
            word = word[1:]
            (row,col)=position

            if row <0 or row>=len_row or col <0 or col >=len_col:
                return False
            position_char = board[row][col]

            if char !=position_char:
                return False
            board[row][col]=""

            if len(word)==0:
                return True

            res = bool    
            res= dfs(board,(row+1,col),word) or  dfs(board,(row-1,col),word) or  dfs(board,(row,col+1),word)  or  dfs(board,(row,col-1),word) 
            board[row][col]=position_char
            return res
        
        for row in range(len_row):
            for col in range(len_col):
                if dfs(board,(row,col),word):
                    return True
        return False
