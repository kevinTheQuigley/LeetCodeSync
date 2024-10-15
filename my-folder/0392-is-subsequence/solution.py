class Solution(object):
    def isSubsequence(self, subString, target):

        if len(subString)==0:
            return True
        j = 0 
        for i in range(len(target)):
            temp = subString[j]
            if target[i] == subString[j]:

                j+=1
            if j == len(subString):
                return True
        return False


        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
