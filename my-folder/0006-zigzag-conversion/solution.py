'''
What could make sense is generating a subList within our main list, and appending the appropriate value
What is the pattern for appending the values of out of order?
The rest can be appended as is
So I think the mod happens like this, remove the top and bottom rows,
so for 1 it's 1:- 1 row
for 2 it's 2:-    2 rows. [a,c,e,g]
for 3 it's 4 rows, but the rows in the middle get re-added; 
use mod to check if it's greater then num rows


i =0, row =0
i = 1,row = 1
...
i =4, row =2
i =5, row =1

'''
class Solution(object):
    def convert(self, s, numRows):
        matrix = []
        for row in range(numRows):
            matrix.append("")
        
        if numRows>2:
            modder = numRows +numRows-2
        else:
            modder = numRows

        for i,letter in enumerate(s):
            
            row = i % modder
            if row>numRows-1:
                row = modder-row
            matrix[row]+= letter
        returnString = ""
        for row in matrix:
            returnString+=row
            
        return returnString

        
        

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
