class Solution(object):
    def twoSum(self, numbers, target):
        posDict = {}
        for i,num in enumerate(numbers):
            numTarget = target-num
            if numTarget in posDict:
                return(posDict[numTarget],i+1)
            else:
                posDict[num]=i+1

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
