class Solution(object):
    def singleNumber(self, nums):
        generalDict = {}

        for num in nums:
            if not generalDict.get(num):
                generalDict[num]=1
            elif generalDict[num]==1:
                generalDict[num]=2
            elif generalDict[num]==2:
                generalDict.pop(num)
        value = generalDict.keys()[0]
        return value

        """
        :type nums: List[int]
        :rtype: int
        """
        
