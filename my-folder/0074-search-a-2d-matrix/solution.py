class Solution(object):
    def searchMatrix(self, matrix, target):
        columns = len(matrix[0])
        rows = len(matrix)
        
        topPointer = 0
        bottomPointer = rows-1

        leftPointer = 0
        rightPointer = columns-1

        middle = int((topPointer +bottomPointer)/2)
        while topPointer <=   bottomPointer:
            middle = int((topPointer +bottomPointer)/2)
            print(middle,topPointer,bottomPointer)
            
            if (matrix[middle][0] > target):
                bottomPointer = middle-1
                middle = middle-1
            elif (matrix[middle][0] < target):
                topPointer = middle +1

            else:
                return True
        print(middle)
        while leftPointer <= rightPointer:
            center = int((leftPointer + rightPointer)/2)
            print(center,leftPointer,rightPointer)
            if (matrix[middle][center])>target:
                rightPointer =center -1
            elif (matrix[middle][center])<target:
                leftPointer = center +1
            else:
                return True
        else:
            return False

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    

