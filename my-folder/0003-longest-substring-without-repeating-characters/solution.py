class Solution(object):
    def lengthOfLongestSubstring(self, inputString):

        repeatDict = {}
        repeatString = ""
        repeatLength = 0
        maxRepeat = 0
        if len(inputString)==0:
            return repeatLength

        for i in range(len(inputString)):
            j = i
            length = 0 
            while j < len(inputString):
                if inputString[j] in repeatDict:
                    break
                length +=1
                
                maxRepeat = max(length,maxRepeat)
                repeatDict[inputString[j]] =True
                j+=1
            repeatDict = {}
        
        return maxRepeat

        """
        :type s: str
        :rtype: int
        """
        
