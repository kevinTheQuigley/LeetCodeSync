class Solution:
    def solve(self, board: List[List[str]]) -> None:

        daList=[]
        c="C"
        o="O"
        x="X"
        i_len = len(board)
        j_len = len(board[0])

        def inBounds(i,j):
            if ((i>=0) and (i <i_len)) and ((j>=0)and (j<j_len)):
                return True

        for i in range(len(board)):
            if board[i][0]==o:
                daList.append((i,0))
            if board[i][j_len-1]==o:
                daList.append((i,j_len-1))

        for j in range(len(board[0])):
            if board[0][j]==o:
                daList.append((0,j))
            if board[i_len-1][j]==o:
                daList.append((i_len-1,j))

        while daList:
            checkList= []
            (i,j) = daList.pop()
            board[i][j]=c
            checkList.extend([(i+1,j),(i-1,j),(i,j-1),(i,j+1)])

            for (ii,jj) in checkList:
                if inBounds(ii,jj):
                    if board[ii][jj]==o:
                        daList.append((ii,jj))

        for i in range(i_len):
            for j in range(j_len):
                if board[i][j]==o:
                    board[i][j]=x
                if board[i][j]==c:
                    board[i][j]=o

        return board

