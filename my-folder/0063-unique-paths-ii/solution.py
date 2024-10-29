class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        columns,rows = len(obstacleGrid[0])-1,len(obstacleGrid)-1
        pathDict = {}
        

        def dfs(column,row):
            pathString = (str(column)+"_"+str(row))
            if pathString in pathDict:
                return pathDict[pathString]
            if obstacleGrid[row][column] ==1:
                return 0
            elif row == rows and column ==columns:
                return 1
            else:
                count = 0
                if column <columns:
                    count += dfs(column+1,row)
                if row <rows:
                    count+=dfs(column,row+1)

            pathDict[pathString] = count
            return count
        
        return dfs(0,0)



