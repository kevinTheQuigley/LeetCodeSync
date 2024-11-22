'''
Do I need to just iterate through all values in the matrix?
pair list of locations to change, record them, change them after?

for i in row:
    for j in column:
        if ..==0:
            pairs.append([i,j])
for pair in pairs:
    matrix[i][:]=0
    matrix[:][j]=0

'''


class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        zeroRows = []
        zeroColumns = []
        for row in range(rows):
            for column in range(columns):
                if matrix[row][column]==0:
                    zeroRows.append(row)
                    zeroColumns.append(column)
        zeroRows = set(zeroRows)
        zeroColumns = set(zeroColumns)

        for row in range(rows):
            for column in range(columns):
                if row in zeroRows:
                    matrix[row][column]=0
                if column in zeroColumns:
                    matrix[row][column]=0

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        
