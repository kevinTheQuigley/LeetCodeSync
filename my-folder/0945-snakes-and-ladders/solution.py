class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)

        def numToPosition(num):
            ypos = (n - 1) - (num - 1) // n

            if n%2 ==0:
                if ypos % 2 ==1:  
                    xpos = (num - 1) % n
                else:  
                    xpos = (n - 1) - ((num - 1) % n)
            else:
                if ypos % 2 ==0:  
                    xpos = (num - 1) % n
                else:  
                    xpos = (n - 1) - ((num - 1) % n)
            
            return [ypos, xpos]
        
        def atEnd(num):
            if num >=n*n:
                return True

        from collections import deque
        theDeque = deque()
        theDeque.append([1,0])
        visited = set()

        while len(theDeque)>0:
            [num,count] = theDeque.popleft()
            count+=1
            
            
            for i in range(1,7):
                newNum = i+num
                if newNum in visited:
                    continue
                visited.add(newNum)

                if atEnd(newNum):
                    return count

                position = numToPosition(newNum)
                if board[position[0]][position[1]] !=  -1:
                    newNum = board[position[0]][position[1]] 
                    position = numToPosition(newNum)


                    if atEnd(newNum):
                        return count

 
                theDeque.append([newNum,count])

            
            
        


        return -1  # If the end is not reachable

