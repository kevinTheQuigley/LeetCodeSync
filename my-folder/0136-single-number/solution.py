class Solution(object):
    def singleNumber(self, nums):
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num]=True
            else:
                numDict.pop(num)
        return list(numDict.keys())[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        
