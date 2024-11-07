'''

in example 1

[0][0] -> [0][2]
[0][1] -> [1][2]
[0][2] -> [2][2]

[1][0] -> [0][1]
[1][1] -> [1][1]
[1][2] -> [2][1]

[2][0] -> [0][0]
[2][1] -> [1][0]
[2][2] -> [2][0]

for the index i,j, i become 2-i, and j become i. 

li[0] = li[2][0],li[1][0],li[0][0]
li[1] = [2][1],[1][1],[0][1]

'''

class Solution(object):
    def rotate(self, matrix):
        # Create a rotated version in `res`
        res = [[matrix[len(matrix) - 1 - i][j] for i in range(len(matrix))] for j in range(len(matrix))]
        
        # Copy elements from `res` back to `matrix` to modify it in place
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = res[i][j]



        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
