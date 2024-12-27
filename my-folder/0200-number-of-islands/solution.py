



class Solution(object):
    def numIslands(self, grid):
        counter = 0 

        def convertIsland(i,j):
            if (0<=i<len(grid)) and (0<=j<len(grid[0])):
                if grid[i][j] =="1":
                    grid[i][j]="2"
                    convertIsland(i+1,j)
                    convertIsland(i-1,j)
                    convertIsland(i,j+1)
                    convertIsland(i,j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    counter+=1
                    convertIsland(i,j)
                    
        return counter

            

                
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
