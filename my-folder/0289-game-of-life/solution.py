'''
What about just using placeholders to indicate what's going to happen next?
We have 1,0 - AliveNow, DeadNow
Move to 3,2 - dead going to be Alive, alive going to be dead?




'''
class Solution(object):
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])
        def checkCell(row,column):

            if row ==0:
                rowStart = 0
            else:
                rowStart = row-1
            if row == rows-1:
                rowEnd = rows-1
            else:
                rowEnd = row+1

            if column ==0:
                columnStart = 0
            else:
                columnStart = column-1

            if column == cols-1:
                columnEnd = column
            else:
                columnEnd = column+1
            aliveTotal = 0

            for i in range(rowStart,rowEnd+1):
                for j in range(columnStart,columnEnd+1):
                    if not (i ==row and j==column):
                        pos = board[i][j]
                        if pos ==1 or pos ==2:
                            aliveTotal+=1
            print(aliveTotal)
            currentState = board[row][column]                
            if (aliveTotal <2 and currentState ==1) or (aliveTotal >3 and currentState ==1):
                board[row][column] =2

            elif currentState ==0 and aliveTotal==3:
                board[row][column] = 3

                        


            


        for row in range(rows):
            for column in range(cols):
                checkCell(row,column)
        
        for row in range(rows):
            for column in range(cols):
                if board[row][column]==2:
                    board[row][column]=0
                elif board[row][column]==3:
                    board[row][column]=1
        

        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
