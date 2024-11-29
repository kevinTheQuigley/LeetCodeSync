'''
start with lowestRow,lowestColumn,highestRow,highestColumn = 0,0,2,2

Step 1: Iterate right, if row>highestRow
row = 0, column = 0 -> iterate until column = maxColumn, increase lowestRow by 1
row = 0, column = 2 -> up until row..., increase lowestRow by 1
..repet until position =lR,lC = hR,hC

0>1 0 added
1>2 1 added
2>3 2 added
Pointer is left above, so reduce it?



'''

class Solution(object):
    def spiralOrder(self, matrix):
        lr,lc,hr,hc = 0,0,len(matrix)-1,len(matrix[0])-1
        i,j = 0,0
        returnList = []
        while lr<=hr or lc<=hc:
            if lr<=hr:
                while i<=hc:
                    returnList.append(matrix[j][i])
                    i =i+1
                i-=1
                j+=1
            
            lr+=1

            if lc<=hc:
                while j<= hr  :
                    print(i,j)
                    returnList.append(matrix[j][i])
                    j = j+1  
                j-=1 
                i-=1
            hc-=1

            if lr<=hr:
                while i>= lc:
                    returnList.append(matrix[j][i])
                    i=i-1
                i+=1
                j-=1  
            hr-=1

            if lc<=hc :
                while j>= lr:
                    returnList.append(matrix[j][i])
                    j=j-1
                j+=1
                i+=1
            lc+=1   


        return returnList            

        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
