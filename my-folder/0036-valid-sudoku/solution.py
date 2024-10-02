class Solution(object):
    def isValidSudoku(self, board):
        lines = []
        columns = []
        squares = []

        for i in range(9):
            squares.append(9*[0])
            columns.append(9*[0])
            lines.append(9*[0])


        for i in range(9):
            for j in range(9):
                value = (board[i][j])
                if value != ".":
                    value = int(value)-1
                    ival = int(i/3)
                    jval = int(j/3)*3
                    total = ival+jval
                    if squares[total][value] ==0:
                        squares[total][value] = 1
                        #print("converting square No."+str(total)+" to value "+str(value))
                    else:
                        print(i,j)
                        print("Square No."+str(total)+" Already has "+str(value))
                        return False
                    

                    if lines[i][value] ==0:
                        lines[i][value] = 1
                        #print("converting Line No."+str(total)+" to value "+str(value))
                    else:
                        print(i,j)
                        print("Line No."+str(total)+" Already has "+str(value))
                        return False

                    if columns[j][value] ==0:
                        #print("converting Col No."+str(total)+" to value "+str(value))
                        columns[j][value] = 1
                    else:
                        print(i,j)
                        print("column No."+str(total)+" Already has "+str(value))
                        return False
                
        return True
                    
        """
        :type board: List[List[str]]
        :rtype: bool
        """

